# AI/LLM/Agents Intelligence Tracker

A continuously-updated awareness index of AI agent frameworks, designed to be queried by LLMs
and coding agents whose training data has a knowledge cutoff.

**The problem it solves:** AI moves fast, and LLMs are generally unaware of frameworks and
approaches that emerged after their training cutoff. This pipeline builds a knowledge base that
gives an agent *awareness that something exists, what it does, and how it broadly works* —
plus a citation to the primary source so it can verify current details on demand.

This is also a practice run for a monitoring pipeline architecture being considered for a
pharmaceutical client (regulatory change tracking → structured knowledge base → analysis agent).

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

**Popular (weekly):** established frameworks with >3000 stars  
**Emerging (daily):** repos created in the last 30 days with >50 stars

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

4. **`scripts/github_filter.py --reject owner/repo1 ...`** (out-of-scope repos)
   - Adds to `scripts/github_rejected.json` — skipped in all future runs

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

**Status: pending** — `sources/` populated, compile not yet run in its final form.

`llm-wiki-compiler` ingests `sources/` and builds a structured, interlinked wiki:
- Hash-based incremental ingestion — only re-processes changed files
- Content-aware deduplication — concepts shared across READMEs merge into single pages
- Citations trace every wiki page back to its source file
- `llmwiki query` / `llmwiki context` provide hybrid semantic + BM25 + graph retrieval
- MCP server exposes the query interface directly to coding agents

Config: `OPENAI_API_KEY`, `LLMWIKI_PROVIDER`, `LLMWIKI_MODEL` in `.env` (loaded via `.envrc`)

---

## Repo structure

```
sources/                        flat markdown files (one per scraped repo)
  github-<owner>_<repo>.md      YAML frontmatter + verbatim README
prompts/
  github_frameworks_popular.md  Hermes prompt for weekly popular-frameworks run
  github_frameworks_emerging.md Hermes prompt for daily emerging-frameworks run
scripts/
  github_filter.py              GitHub API fetch + change-detection + rejection filter
  github_write.py               README fetch + source file writer (no LLM involved)
  github_rejected.json          persistent list of out-of-scope repos (never re-evaluated)
  ingest_all.sh                 bootstrap loop for initial ingestion
wiki/                           llm-wiki-compiler output (compiled knowledge base)
docs/
  initial_plan.md               full background, architecture decisions, open questions
```
