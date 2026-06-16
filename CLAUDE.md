# AI/LLM/Agents Intelligence Tracker

Practice project for a pharma-industry monitoring pipeline pattern, applied to the AI/agents domain.
Full background and architecture: see `docs/initial_plan.md`.

## Pipeline

```
Hermes (scrape/extract, scheduled) -> /sources (markdown + frontmatter) -> WikiLLM (structure/dedupe) -> query agent
```

**Core design principle (separation of concerns):** Hermes only searches, extracts, and formats —
it never summarizes or edits source content. Summarization/synthesis happens downstream
(WikiLLM ingestion / query agent), so `/sources` always contains untouched source material.

Note: `/sources` is named to match `llm-wiki-compiler`'s expected project layout (it reads from
a `sources/` directory at the project root). It was originally called `/raw` in early planning —
renamed for direct compatibility, avoiding a symlink (which `llmwiki` excludes as "out-of-tree").

## Status

- [x] Hermes installed and configured locally
- [x] arXiv research-track validated (70+ papers in `sources/arxiv-*.md`)
- [x] WikiLLM implementation chosen: `llm-wiki-compiler`
- [x] GitHub framework discovery track designed and implemented (`scripts/`)
- [x] GitHub popular track initial run done (~84 files in `sources/github-*.md`)
- [ ] GitHub emerging track not yet tested
- [ ] `llm-wiki-compiler` compile against current `/sources` pending
- [ ] Cron automation (gateway) not yet enabled — `hermes gateway install` still needed
- [ ] Query agent

## Hermes setup notes

- Model: **o4-mini** via OpenAI (`openai-api`, endpoint `https://api.openai.com/v1`)
  - gpt-4o / gpt-4o-mini fail with this Hermes version: it unconditionally sends
    `include: ["reasoning.encrypted_content"]`, which only o-series reasoning models support
    (known bug, [NousResearch/hermes-agent#23450](https://github.com/NousResearch/hermes-agent/issues/23450), no config workaround)
  - o-series models additionally require **OpenAI org verification** for reasoning summaries
    (platform.openai.com/settings/organization/general) — done
- Terminal backend: **local**
- Browser backend: **Local Browser** (headless Chromium, free)
- Search/extract provider: **Parallel** (free, no API key needed for base usage)
- Tools: defaults, except Computer Use (macOS) disabled (platform-irrelevant on WSL2)

## `/sources` output format

One markdown file per item, in a flat `sources/` directory (required by `llm-wiki-compiler` —
it does not recurse into subdirectories and rejects symlinks, even in-tree ones). Filenames
are prefixed by source type and the stable source ID, e.g. `sources/arxiv-<arxiv_id>.md`, so
re-scraping the same item overwrites the file — free dedup, no extra logic needed, while
keeping provenance visible in the filename (also recorded in the `source` frontmatter field).
Dedup *across sources* is WikiLLM's job at ingestion.

### arXiv frontmatter schema

```yaml
---
title: "..."
arxiv_id: "2506.12345v1"
authors: ["...", "..."]
submitted: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
categories: ["cs.AI", "cs.CL"]
primary_category: "cs.AI"
abs_url: "https://arxiv.org/abs/<id>"
pdf_url: "https://arxiv.org/pdf/<id>"
source: arxiv
scraped_at: "<ISO 8601 UTC>"
---
<abstract verbatim>
```

### GitHub frontmatter schema

```yaml
---
name: "<repo name without owner>"
repo: "<owner>/<repo>"
url: "https://github.com/<owner>/<repo>"
description: "<repo description>"
stars: <int>
language: "<primary language>"
topics: ["...", "..."]
created_at: "YYYY-MM-DD"
pushed_at: "YYYY-MM-DD"
source: github
scraped_at: "<ISO 8601 UTC>"
---
<README verbatim>
```

## arXiv research track

- Prompt: `prompts/arxiv_research.md` (self-contained — cron jobs run in fresh sessions, so it
  includes all instructions, no chat context)
- Logic:
  1. Get current UTC date via `date` shell command (not LLM's internal date sense — unreliable)
  2. Query arXiv API directly with `cat:cs.AI OR cat:cs.CL` + `submittedDate` range for last
     3 days (mechanical filtering pushed to arXiv's API, not done by the LLM)
  3. Hermes makes a semantic in-scope/out-of-scope judgment per paper based on title+abstract,
     using the scope definition from `docs/initial_plan.md` (NOT simple keyword matching —
     that's brittle and underuses the LLM's actual strength)
  4. Writes one markdown file per in-scope paper to `sources/arxiv-<arxiv_id>.md`
- 3-day lookback (not "today only") deliberately overlaps runs — covers late-indexed papers.
  Combined with ID-based filenames, overlap costs nothing.
- Cron job created (`hermes cron create "0 7 * * *" ...`, daily 07:00) but **gateway not yet
  running** — job won't fire automatically until `hermes gateway install` is run.

## GitHub framework discovery track

Two cadences driven by a mode preset (implementation detail hidden from the LLM prompt):

- **Popular** (`--mode popular`): min 3000 stars, no date filter, weekly cadence
- **Emerging** (`--mode emerging`): min 50 stars, created within last 30 days, daily cadence

Topics queried (one GitHub Search API call per topic, paginated for full coverage, then merged
and deduped): `llm-agent`, `ai-agent`, `agent-framework`, `autonomous-agents`,
`multi-agent-systems`, `llm-agents`.

### Two-script architecture (key design decision)

README content must never pass through the LLM's context window (cost + context size).
The LLM only handles semantic in/out-of-scope judgment:

- **`scripts/github_filter.py --mode <mode>`**: fetches candidates from GitHub API, applies
  two mechanical pre-filters (change-detection via `pushed_at`, rejection list), fetches first
  ~2 KB of README as preview for LLM judgment. Caches full metadata to
  `/tmp/github_candidates.json`. Capped at 20 candidates per run (batching).
- **Hermes (LLM)**: judges in/out of scope from `description` + `topics` + `readme_preview`
- **`scripts/github_write.py owner/repo ...`**: for in-scope repos — reads cache, fetches full
  README, writes `sources/github-<owner>_<repo>.md`. No LLM involved.
- **`scripts/github_filter.py --reject owner/repo ...`**: records out-of-scope repos to
  `scripts/github_rejected.json` — permanently skipped in all future runs.

### Prompts

- `prompts/github_frameworks_popular.md` — weekly popular run
- `prompts/github_frameworks_emerging.md` — daily emerging run

Both include "do not ask for confirmation / do not narrate" instructions at the top (Hermes
would otherwise pause on large candidate lists).

### Initial ingestion

For the first run (large backlog), loop until filter returns empty:
```bash
./scripts/ingest_all.sh  # loops hermes run until no new files or rejections
```

### Cleanup needed

`scripts/github_pipeline.py` is an outdated file from early experimentation (keyword-based
in_scope filter, fetches full README — both superseded). Safe to delete.

## WikiLLM: `llm-wiki-compiler`

Chosen over `nvk/llm-wiki` (which is a Claude Code/Codex plugin driven via slash commands,
less suited to a headless pipeline). `llm-wiki-compiler`:
- Standalone Node.js CLI/SDK (Node >=24), supports OpenAI as provider (configured via
  `.env` + `.envrc`/direnv: `OPENAI_API_KEY`, `LLMWIKI_PROVIDER`, `LLMWIKI_MODEL`)
- Hash-based incremental ingestion + content-aware deduplication
- Built-in `llmwiki query` (hybrid semantic + BM25 + graph retrieval) — candidate to double
  as the query-agent layer for this prototype
- Project root is the repo root (`.llmwiki/`, `sources/`, compiled `wiki/` all live there) —
  required because `llmwiki` reads `sources/` non-recursively and rejects all symlinks
  (even in-tree), so source files must be real, flat files directly in `sources/`
- Compile pending against current `sources/` (arXiv + GitHub combined)
