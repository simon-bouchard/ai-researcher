#!/usr/bin/env python3
"""
Fetch full READMEs and write sources/github-<owner>_<repo>.md files for
repos judged in-scope by the LLM. Also records out-of-scope repos to the
rejection list so they are skipped in future filter runs.

Reads repo metadata from the filter cache (/tmp/github_candidates.json).
Falls back to querying the GitHub API directly if a repo is not in the cache.

Usage:
  github_write.py "owner/repo1" "owner/repo2" ...          # write in-scope repos
  github_write.py --reject "owner/repo1" "owner/repo2" ... # record out-of-scope repos
"""

import argparse
import datetime
import json
import os
import sys
import time
import urllib.request

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)
SOURCES_DIR = os.path.join(REPO_ROOT, "sources")
CANDIDATES_CACHE = "/tmp/github_candidates.json"
REJECTED_FILE = os.path.join(SCRIPTS_DIR, "github_rejected.json")

_first_request = True


def fetch(url):
    global _first_request
    if not _first_request:
        time.sleep(2)
    _first_request = False
    req = urllib.request.Request(url, headers={"User-Agent": "ai-researcher-hermes"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def load_cache():
    if not os.path.exists(CANDIDATES_CACHE):
        return {}
    with open(CANDIDATES_CACHE, "r", encoding="utf-8") as f:
        items = json.load(f)
    return {item["full_name"]: item for item in items}


def fetch_repo_meta(full_name):
    url = f"https://api.github.com/repos/{full_name}"
    data = json.loads(fetch(url))
    return {
        "full_name": data["full_name"],
        "html_url": data["html_url"],
        "description": data["description"],
        "stargazers_count": data["stargazers_count"],
        "language": data["language"],
        "topics": data.get("topics", []),
        "created_at": data["created_at"][:10],
        "pushed_at": data["pushed_at"][:10],
        "default_branch": data["default_branch"],
        "scraped_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def fetch_readme(full_name, default_branch):
    for filename in ("README.md", "README.rst", "Readme.md", "readme.md"):
        url = f"https://raw.githubusercontent.com/{full_name}/{default_branch}/{filename}"
        try:
            return fetch(url).decode("utf-8", errors="replace")
        except Exception:
            continue
    return ""


def write_source(meta, readme):
    owner, repo = meta["full_name"].split("/", 1)
    filename = f"github-{owner}_{repo}.md"
    path = os.path.join(SOURCES_DIR, filename)

    topics_yaml = json.dumps(meta["topics"])
    scraped_at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # sanitize description to avoid backslashes in f-string expressions
    safe_description = (meta.get("description") or "").replace('"', '\\"')

    content = f"""---
name: "{repo}"
repo: "{meta['full_name']}"
url: "{meta['html_url']}"
description: "{safe_description}"
stars: {meta['stargazers_count']}
language: "{meta['language'] or ''}"
topics: {topics_yaml}
created_at: "{meta['created_at']}"
pushed_at: "{meta['pushed_at']}"
source: github
scraped_at: "{scraped_at}"
---

{readme.strip()}
"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {filename} ({len(readme)} chars)")


def load_rejected():
    if not os.path.exists(REJECTED_FILE):
        return set()
    with open(REJECTED_FILE, "r", encoding="utf-8") as f:
        return set(json.load(f))


def save_rejected(rejected_set):
    with open(REJECTED_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(rejected_set), f, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repos", nargs="*", metavar="owner/repo")
    parser.add_argument("--reject", nargs="+", metavar="owner/repo")
    args = parser.parse_args()

    if args.reject:
        rejected = load_rejected()
        rejected.update(args.reject)
        save_rejected(rejected)
        print(f"  recorded {len(args.reject)} rejection(s)")
        return

    if not args.repos:
        parser.print_usage(sys.stderr)
        sys.exit(1)

    cache = load_cache()
    for full_name in args.repos:
        print(f"Processing {full_name}...")
        meta = cache.get(full_name) or fetch_repo_meta(full_name)
        readme = fetch_readme(full_name, meta["default_branch"])
        write_source(meta, readme)


if __name__ == "__main__":
    main()
