# AI/LLM/Agents Intelligence Tracker

Practice project for a pharma-industry monitoring pipeline pattern, applied to the AI/agents domain.
Full background and architecture: see `docs/initial_plan.md`.

## Pipeline

```
Hermes (scrape/extract, scheduled) -> /sources (markdown + frontmatter) -> update_topic_hints.py -> WikiLLM (structure/dedupe) -> query agent
```

**Core design principle (separation of concerns):** Hermes only searches, extracts, and formats —
it never summarizes or edits source content. Summarization/synthesis happens downstream
(WikiLLM ingestion / query agent), so `/sources` always contains untouched source material.

Note: `/sources` was originally called `/raw` in early planning — renamed when the first WikiLLM
implementation was chosen. The current implementation (ussumant/llm-wiki-compiler) configures
source paths in `.wiki-compiler.json`, so `sources/` is now just the established convention.

## Status

- [x] Hermes installed and configured locally
- [x] WikiLLM implementation chosen: `ussumant/llm-wiki-compiler` (Claude Code plugin)
- [x] GitHub framework discovery track designed and implemented (`scripts/`)
- [x] WikiLLM: plugin installed, `/llm-wiki-compiler:wiki-init` done, `wiki/schema.md` configured
- [x] Orchestration: Airflow (standalone) set up locally with two DAGs — popular (weekly) + emerging (daily)
- [x] First end-to-end pipeline run via Airflow validated
- [ ] Star thresholds conservatively set for testing (popular: 10k, emerging: 500); target production values: popular ~1000, emerging 50–100
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
- Invocation (v0.16.0): `hermes run` was removed — use `hermes chat --cli -Q --yolo -q "$(cat prompt_file)"`.
  `--cli` avoids TUI, `-Q` suppresses banner/spinner for scripting, `--yolo` auto-accepts tool calls.

## `/sources` output format

One markdown file per repo, in a flat `sources/` directory (path configured in `.wiki-compiler.json`). Filenames
use the pattern `github-<owner>_<repo>.md`, so re-scraping the same repo overwrites the file —
free dedup, no extra logic needed. Dedup across sources is WikiLLM's job at ingestion.

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

## GitHub framework discovery track

Two cadences driven by a mode preset (implementation detail hidden from the LLM prompt):

- **Popular** (`--mode popular`): min 10000 stars (test; target ~1000 for production), no date filter, weekly cadence
- **Emerging** (`--mode emerging`): min 500 stars (test; target 50–100 for production), created within last 30 days, daily cadence

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
- **`scripts/github_write.py --reject owner/repo ...`**: records out-of-scope repos to
  `scripts/github_rejected.json` — permanently skipped in all future runs.
  (Reject logic lives in `github_write.py`, not `github_filter.py` — filter is purely read/query.)
- **`scripts/update_topic_hints.py`**: syncs `.wiki-compiler.json` `topic_hints` from
  `sources/` filenames using `owner_repo` slugs (lowercased) — guarantees uniqueness across
  repos with identical names. Run after Hermes, before `/llm-wiki-compiler:wiki-compile`.

### Prompts

- `prompts/github_frameworks_popular.md` — weekly popular run
- `prompts/github_frameworks_emerging.md` — daily emerging run

Both include "do not ask for confirmation / do not narrate" instructions at the top (Hermes
would otherwise pause on large candidate lists).

### Initial ingestion

For the first run (large backlog), loop until filter returns empty:
```bash
./scripts/ingest_all.sh  # loops hermes chat until no new files or rejections
```

## Orchestration: Airflow

Airflow (standalone mode) runs locally and schedules the full pipeline. Two DAGs in `dags/github_frameworks.py`:

- **`github_frameworks_popular`** — weekly, min 10k stars
- **`github_frameworks_emerging`** — daily, min 500 stars, last 30 days

Each DAG runs three tasks in sequence:
```
ingest (ingest_all.sh)  →  update_topic_hints (update_topic_hints.py)  →  compile_wiki (claude -p "...")
```

### Local setup

```bash
# Install (once)
uv venv .venv && source .venv/bin/activate && uv pip install apache-airflow

# Required env vars (in .env, picked up by direnv)
AIRFLOW_HOME=/home/simon/documents/ai-researcher/.airflow
AIRFLOW__CORE__DAGS_FOLDER=/home/simon/documents/ai-researcher/dags

# Start
airflow standalone   # admin password written to .airflow/standalone_admin_password.txt
# Web UI at http://localhost:8080
```

`.venv/` and `.airflow/` are gitignored — local only.

## WikiLLM: `ussumant/llm-wiki-compiler`

Chosen over `atomicstrata/llm-wiki-compiler` (standalone Node.js CLI) because the standalone
tool has a hardcoded extraction prompt with no customization mechanism — all extracted pages
receive the same `defaultKind`, and schema `kinds` descriptions are never injected into any
extraction or page-writing prompt. The Claude Code plugin approach gives full control over
extraction via a natural language `schema.md` that the compiler reads before every run.

- **Claude Code plugin** — invoked via slash commands (`/llm-wiki-compiler:wiki-init`, `/llm-wiki-compiler:wiki-compile`, `/llm-wiki-compiler:wiki-query`)
- **Customizable extraction:** `schema.md` (natural language, in `wiki/schema.md`) defines
  entity types, tagging conventions, article structure, and cross-reference rules — the compiler
  reads and respects it on every run
- **Config:** `.wiki-compiler.json` at project root — source paths, article sections, topic hints
- **Topic slugs:** `owner_repo` format (lowercased), e.g. `nousresearch_hermes-agent` — guarantees uniqueness
- **Incremental:** only recompiles topics whose source files changed
- **Automated via Airflow:** `claude -p "/llm-wiki-compiler:wiki-compile"` runs fully autonomously
  as the final task of each DAG run

### CLAUDE.md vs wiki/schema.md separation

Both files are loaded during a Claude Code compile session (CLAUDE.md files are additive, not
replacing — a `wiki/CLAUDE.md` would stack on top of root CLAUDE.md, not replace it). This means:

- **`CLAUDE.md`** (this file) — developer instructions for Claude Code when working on the
  project. Keep it dev-focused. Avoid instructions that could conflict with autonomous
  compilation (e.g. "always confirm before writing files").
- **`wiki/schema.md`** — wiki compilation schema read by the compiler on every run. All domain
  conventions belong here, not in CLAUDE.md.

### Setup workflow (completed)

1. Install plugin: `ussumant/llm-wiki-compiler` added to Claude Code plugins
2. Run `/llm-wiki-compiler:wiki-init` interactively — wrote `.wiki-compiler.json` with 8-section
   article structure (Summary, Core Pattern, Key Features, Tech Stack, Traction, Use Cases,
   Related Frameworks, Sources) and `owner_repo` topic slug convention
3. First compile generated `wiki/schema.md` as a draft
4. Edited `wiki/schema.md`: cleared stale topic/concept registry, kept structural conventions;
   added status convention for deprecated/superseded frameworks (tag in Summary + successor link
   in Related Frameworks)
5. Subsequent compiles run via Airflow — no manual steps needed

### Ongoing: run `scripts/update_topic_hints.py` before each compile
Keeps `topic_hints` in `.wiki-compiler.json` in sync with `sources/` filenames.
