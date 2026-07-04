#!/usr/bin/env python3
"""
Query GitHub's repository search API for AI agent frameworks (one query per
topic, paginated to get all matching results), merge and dedupe across
topics, then filter out repos that are already handled:
  - repos previously judged out-of-scope (recorded in scripts/github_rejected.json)
  - repos in sources/github-<owner>_<repo>.md with an unchanged pushed_at
  - repos in sources/ that were modified but scraped less than --reingest-after-days ago

For each remaining candidate, fetches the first ~2 KB of the README so the
LLM can make an accurate in/out-of-scope judgment without reading the full file.

Results are printed as JSON and cached to /tmp/github_candidates.json for
github_write.py to read after the LLM selects the in-scope repos.

Usage:
  # Filter run via mode preset (for use in Hermes prompts)
  github_filter.py --mode popular|emerging

  # Filter run with explicit parameters (for scripting/testing)
  github_filter.py --min-stars N [--created-after-days N] [--reingest-after-days N] [--limit N] [--topics t1,t2,...]

Mode presets:
  popular:  --min-stars 10000 --reingest-after-days 60 --limit 20
  emerging: --min-stars 500 --created-after-days 30 --limit 20
"""

import argparse
import datetime
import json
import os
import re
import time
import urllib.parse
import urllib.request

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)
SOURCES_DIR = os.path.join(REPO_ROOT, "sources")
REJECTED_FILE = os.path.join(SCRIPTS_DIR, "github_rejected.json")
CANDIDATES_CACHE = "/tmp/github_candidates.json"

DEFAULT_TOPICS = [
    "llm-agent",
    "ai-agent",
    "agent-framework",
    "autonomous-agents",
    "multi-agent-systems",
    "llm-agents",
]

_first_search_request = True


def load_rejected():
    if not os.path.exists(REJECTED_FILE):
        return set()
    with open(REJECTED_FILE, "r", encoding="utf-8") as f:
        return set(json.load(f))



def existing_source_info(full_name):
    """Return (pushed_at, scraped_at) from existing source file, or (None, None) if not found."""
    filename = "github-" + full_name.replace("/", "_") + ".md"
    path = os.path.join(SOURCES_DIR, filename)
    if not os.path.exists(path):
        return None, None
    pushed_at = None
    scraped_at = None
    with open(path, "r", encoding="utf-8") as f:
        in_frontmatter = False
        for line in f:
            if line.strip() == "---":
                if not in_frontmatter:
                    in_frontmatter = True
                    continue
                else:
                    break
            m = re.match(r'^pushed_at:\s*"?([^"\n]+)"?\s*$', line)
            if m:
                pushed_at = m.group(1).strip()
            m = re.match(r'^scraped_at:\s*"?([^"\n]+)"?\s*$', line)
            if m:
                scraped_at = m.group(1).strip()
    return pushed_at, scraped_at


def fetch_search(url):
    global _first_search_request
    if not _first_search_request:
        time.sleep(6)  # stay under the 10 req/min unauthenticated search rate limit
    _first_search_request = False
    req = urllib.request.Request(url, headers={"User-Agent": "ai-researcher-hermes"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def fetch_readme_preview(full_name, default_branch):
    for filename in ("README.md", "README.rst", "Readme.md", "readme.md"):
        url = f"https://raw.githubusercontent.com/{full_name}/{default_branch}/{filename}"
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "ai-researcher-hermes", "Range": "bytes=0-2047"},
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                content = resp.read(2048).decode("utf-8", errors="replace")
            lines = content.splitlines()
            return "\n".join(lines[:20]).strip()
        except Exception:
            continue
    return ""


def fetch_all(query):
    items = []
    page = 1
    while True:
        params = {"q": query, "sort": "stars", "order": "desc", "per_page": 100, "page": page}
        url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(params)
        data = fetch_search(url)
        page_items = data.get("items", [])
        items.extend(page_items)
        total_count = data.get("total_count", 0)
        if len(page_items) == 0 or len(items) >= total_count or page >= 10:
            break
        page += 1
    return items


def run_filter(args):
    created_after = None
    if args.created_after_days is not None:
        created_after = (
            datetime.datetime.now(datetime.timezone.utc)
            - datetime.timedelta(days=args.created_after_days)
        ).strftime("%Y-%m-%d")

    scraped_at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    rejected = load_rejected()

    merged = {}
    for topic in args.topics.split(","):
        query = f"topic:{topic} stars:>{args.min_stars}"
        if created_after:
            query += f" created:>{created_after}"
        for item in fetch_all(query):
            merged[item["full_name"]] = item

    now = datetime.datetime.now(datetime.timezone.utc)

    candidates = []
    for full_name, item in merged.items():
        if full_name in rejected:
            continue
        current_pushed_at = item["pushed_at"][:10]
        existing_pushed, existing_scraped = existing_source_info(full_name)
        if existing_pushed is not None:
            if existing_pushed == current_pushed_at:
                continue  # unchanged
            if args.reingest_after_days is not None and existing_scraped:
                try:
                    scraped_dt = datetime.datetime.fromisoformat(existing_scraped.replace("Z", "+00:00"))
                    if (now - scraped_dt).days < args.reingest_after_days:
                        continue  # modified but scraped too recently
                except ValueError:
                    pass  # malformed scraped_at — let it through
        candidates.append({
            "full_name": full_name,
            "html_url": item["html_url"],
            "description": item["description"],
            "stargazers_count": item["stargazers_count"],
            "language": item["language"],
            "topics": item["topics"],
            "created_at": item["created_at"][:10],
            "pushed_at": current_pushed_at,
            "default_branch": item["default_branch"],
            "scraped_at": scraped_at,
        })

    if args.limit is not None:
        candidates = candidates[: args.limit]

    # Fetch README previews for the final candidate set
    for i, candidate in enumerate(candidates):
        if i > 0:
            time.sleep(1)
        candidate["readme_preview"] = fetch_readme_preview(
            candidate["full_name"], candidate["default_branch"]
        )

    with open(CANDIDATES_CACHE, "w", encoding="utf-8") as f:
        json.dump(candidates, f)

    print(json.dumps(candidates, indent=2))


def main():
    parser = argparse.ArgumentParser()
    MODE_PRESETS = {
        "popular":  {"min_stars": 10000, "created_after_days": None, "reingest_after_days": 60, "limit": 20},
        "emerging": {"min_stars": 500,   "created_after_days": 30,  "reingest_after_days": None, "limit": 20},
    }

    parser.add_argument("--mode", choices=MODE_PRESETS.keys(),
                        help="preset configuration (for use in Hermes prompts)")
    parser.add_argument("--min-stars", type=int)
    parser.add_argument("--created-after-days", type=int, default=None)
    parser.add_argument("--reingest-after-days", type=int, default=None,
                        help="skip already-ingested repos modified less than N days ago")
    parser.add_argument("--limit", type=int, default=None,
                        help="max candidates to return per run (for batched ingestion)")
    parser.add_argument("--topics", default=",".join(DEFAULT_TOPICS))
    args = parser.parse_args()

    if args.mode or args.min_stars is not None:
        if args.mode:
            preset = MODE_PRESETS[args.mode]
            args.min_stars = args.min_stars or preset["min_stars"]
            if args.created_after_days is None:
                args.created_after_days = preset["created_after_days"]
            if args.reingest_after_days is None:
                args.reingest_after_days = preset["reingest_after_days"]
            if args.limit is None:
                args.limit = preset["limit"]
        run_filter(args)
    else:
        parser.error("provide --mode or --min-stars for filter mode, or --reject for reject mode")


if __name__ == "__main__":
    main()
