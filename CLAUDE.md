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
- [x] GitHub popular track initial run done (~84 files in `sources/github-*.md`)
- [ ] GitHub emerging track not yet tested
- [ ] WikiLLM: install plugin → `/wiki-init` → draft compile → edit `wiki/schema.md` → wipe + recompile
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
- **`scripts/update_topic_hints.py`**: syncs `.wiki-compiler.json` `topic_hints` from
  `sources/` filenames — run after Hermes, before `/wiki-compile`.

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

## WikiLLM: `ussumant/llm-wiki-compiler`

Chosen over `atomicstrata/llm-wiki-compiler` (standalone Node.js CLI) because the standalone
tool has a hardcoded extraction prompt with no customization mechanism — all extracted pages
receive the same `defaultKind`, and schema `kinds` descriptions are never injected into any
extraction or page-writing prompt. The Claude Code plugin approach gives full control over
extraction via a natural language `schema.md` that the compiler reads before every run.

- **Claude Code plugin** — invoked via slash commands (`/wiki-init`, `/wiki-compile`, `/wiki-query`)
- **Customizable extraction:** `schema.md` (natural language, in `wiki/schema.md`) defines
  entity types, tagging conventions, article structure, and cross-reference rules — the compiler
  reads and respects it on every run
- **Config:** `.wiki-compiler.json` at project root — source paths, article sections, topic hints
- **Incremental:** only recompiles topics whose source files changed
- **Automated via cron:** `claude -p "/wiki-compile"` runs fully autonomously once config exists —
  no interactive approval gates after initial setup

### CLAUDE.md vs wiki/schema.md separation

Both files are loaded during a Claude Code compile session (CLAUDE.md files are additive, not
replacing — a `wiki/CLAUDE.md` would stack on top of root CLAUDE.md, not replace it). This means:

- **`CLAUDE.md`** (this file) — developer instructions for Claude Code when working on the
  project. Keep it dev-focused. Avoid instructions that could conflict with autonomous
  compilation (e.g. "always confirm before writing files").
- **`wiki/schema.md`** — wiki compilation schema read by the compiler on every run. All domain
  conventions belong here, not in CLAUDE.md.

### Setup workflow

**Step 1 — Install the plugin**
Add `ussumant/llm-wiki-compiler` to Claude Code plugins.

**Step 2 — Run `/wiki-init` interactively**
Init samples `sources/` and proposes an article structure. Before approving, give it domain
context: each GitHub repo should produce one entity page for the framework itself; cross-cutting
patterns (ReAct, tool-calling, memory approaches, etc.) become separate concept pages. Adjust
the proposed article sections to match — something like: Summary, Core Pattern, Key Features,
Tech Stack, Traction, Use Cases, Related Frameworks, Sources. Init writes `.wiki-compiler.json`.
`topic_hints` is populated automatically by `scripts/update_topic_hints.py` — no manual editing needed.

**Step 3 — First compile (draft run)**
Run `/wiki-compile`. This generates `wiki/schema.md` for the first time. The wiki output at
this stage is a draft — expect imperfect entity/concept classification. The goal of this run
is purely to produce `wiki/schema.md` as a starting point to edit.

**Step 4 — Edit `wiki/schema.md`**
Refine the generated schema to encode domain conventions explicitly:
- Each source file (`github-<owner>_<repo>.md`) → one entity page for that framework
- Cross-cutting architectural patterns appearing across multiple repos → concept pages
- Do not create sub-feature pages for things mentioned in only one repo

**Step 5 — Wipe and recompile**
Delete the draft wiki output and recompile with the corrected schema in place. This is the
first meaningful compile.

**Step 6 — Commit and automate**
Commit `.wiki-compiler.json` + `wiki/schema.md`. Subsequent compiles on any machine:
```bash
claude -p "/wiki-compile"   # fully autonomous, no approval gates
```
