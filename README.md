# AI/LLM/Agents Intelligence Tracker

A continuously-updated awareness index of AI agent frameworks, designed to be queried by LLMs
and coding agents whose training data has a knowledge cutoff.

**The problem it solves:** AI moves fast, and LLMs are generally unaware of frameworks and
approaches that emerged after their training cutoff. This pipeline builds a knowledge base that
gives an agent *awareness that something exists, what it does, and how it broadly works* —
plus a citation to the primary source so it can verify current details on demand.

---

## Pipeline

```
Hermes (scrape/extract, scheduled)
    → sources/  (flat markdown + YAML frontmatter)
        → llm-wiki-compiler (structure, dedupe, interlink)
            → llmwiki query / context / MCP  (query interface for coding agents)
```

**Core design principle — separation of concerns:** Hermes only searches, extracts, and
formats. It never summarizes or paraphrases source content. Summarization and synthesis happen
downstream in llm-wiki-compiler, so `sources/` always contains untouched source material with
clear provenance.

---

## Hermes scraping — GitHub framework discovery

Two cadences, both using the same two-script architecture:

**Popular (weekly):** established frameworks with >10k stars (conservative test threshold; target ~1000 for production)  
**Emerging (daily):** repos created in the last 30 days with >500 stars (target 50–100 for production)

### Two-script architecture

The LLM's role is limited to semantic judgment only — all mechanical work is handled by Python
scripts so that README content never passes through the LLM's context window:

1. **`scripts/github_filter.py --mode popular|emerging`**
   - Queries GitHub Search API (one call per topic, paginated for full coverage)
   - Topics: `llm-agent`, `ai-agent`, `agent-framework`, `autonomous-agents`,
     `multi-agent-systems`, `llm-agents`
   - Filters out repos already in `sources/` with an unchanged `pushed_at` (change-detection)
   - Filters out repos previously judged out-of-scope (`scripts/github_rejected.json`)
   - Fetches first ~2 KB of each candidate's README as a preview for the LLM
   - Returns a JSON array of candidates (capped at 20 per run)
   - Caches full metadata to `/tmp/github_candidates.json` for the write script

2. **Hermes (LLM) judges each candidate** from `description` + `topics` + `readme_preview`

3. **`scripts/github_write.py owner/repo1 owner/repo2 ...`** (in-scope repos)
   - Reads metadata from the filter cache
   - Fetches the full README
   - Writes `sources/github-<owner>_<repo>.md`

4. **`scripts/github_write.py --reject owner/repo1 ...`** (out-of-scope repos)
   - Adds to `scripts/github_rejected.json` — skipped in all future runs
   - (`github_filter.py` is read-only; all writes go through `github_write.py`)

Prompts: `prompts/github_frameworks_popular.md`, `prompts/github_frameworks_emerging.md`

### Initial ingestion

For the first run (large backlog), use the bootstrap script which loops until the filter
returns empty:
```bash
./scripts/ingest_all.sh                          # popular track (default)
./scripts/ingest_all.sh prompts/github_frameworks_emerging.md
```

---

## WikiLLM — llm-wiki-compiler

**Status: running** — 37 topic articles + 6 concept articles compiled, updated on every pipeline run.

`llm-wiki-compiler` (Claude Code plugin) ingests `sources/` and builds a structured, interlinked wiki:
- Schema-driven extraction: `wiki/schema.md` defines entity types, article sections, and cross-reference rules — read by the compiler on every run
- Hash-based incremental compilation — only recompiles topics whose source files changed
- Topic slugs use `owner_repo` format (e.g. `nousresearch_hermes-agent`) for guaranteed uniqueness
- Query interface via `/llm-wiki-compiler:wiki-query`

## Orchestration — Airflow

Two DAGs in `dags/github_frameworks.py` run the full pipeline on schedule:

```
ingest_all.sh  →  update_topic_hints.py  →  claude -p "/llm-wiki-compiler:wiki-compile"
```

- `github_frameworks_popular` — weekly
- `github_frameworks_emerging` — daily

Run locally with `airflow standalone` (see CLAUDE.md for setup).

---

## Repo structure

```
sources/                        flat markdown files (one per scraped repo, gitignored)
  github-<owner>_<repo>.md      YAML frontmatter + verbatim README
prompts/
  github_frameworks_popular.md  Hermes prompt for weekly popular-frameworks run
  github_frameworks_emerging.md Hermes prompt for daily emerging-frameworks run
scripts/
  github_filter.py              GitHub API fetch + change-detection + rejection filter (read-only)
  github_write.py               README fetch + source file writer + rejection recorder
  github_rejected.json          persistent list of out-of-scope repos (never re-evaluated)
  update_topic_hints.py         syncs topic_hints in .wiki-compiler.json from sources/ filenames
  ingest_all.sh                 loops Hermes until filter returns empty
dags/
  github_frameworks.py          Airflow DAGs — popular (weekly) + emerging (daily)
wiki/                           llm-wiki-compiler output (compiled knowledge base)
  schema.md                     extraction schema — edit to refine classification conventions
  topics/                       one article per framework (owner_repo slug)
  concepts/                     cross-cutting pattern articles
docs/
  initial_plan.md               full background, architecture decisions, open questions
```
