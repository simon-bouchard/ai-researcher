# AI/LLM/Agents Intelligence Tracker — Project Description

## Background & Motivation

This project is a practice run for a potential client engagement in the pharmaceutical industry. The client use case involves monitoring regulatory changes and pharmaceutical news, ingesting that information into a structured knowledge base, and using it to assist with marketing analyses.

The core pipeline under consideration for that project is:

- **Hermes** (Nous Research) — an autonomous agent framework used to scrape and monitor the web on a schedule
- **WikiLLM** — a tool that ingests raw documents and builds a structured, queryable wiki-style knowledge base
- **An analysis agent** — sits on top of the knowledge base and answers domain-specific questions

Rather than prototype directly on pharmaceutical data (which is domain-specific, compliance-sensitive, and still loosely defined), this toy project applies the same architecture to a well-understood, fast-moving public domain: **AI/LLM/agent research and tooling**.

---

## Project Goal (revised 2026-06-14)

The original framing — a general "intelligence tracker" answering broad questions about recent
developments — has been refined into a more concrete and actionable goal:

**Build a continuously-updated "awareness index" of the AI agent ecosystem (frameworks +
research), designed to be consulted by LLMs/coding agents whose training data has a knowledge
cutoff.**

The core problem this addresses: AI moves fast, and LLMs are generally unaware of frameworks,
tools, and approaches that emerged after their cutoff, which complicates building agentic
systems with them. This knowledge base aims to close that gap — not by being a perfectly
current technical reference, but by giving an agent **awareness that something exists, what it
does, and how it broadly works**, plus a citation back to the primary source (repo, paper) so
the agent can verify exact current details when it matters.

This means:
1. Continuously monitor the web for new/updated agent frameworks and relevant research
2. Ingest and structure that information into a growing knowledge base, prioritizing **breadth**
   (awareness of what exists) with citations enabling **on-demand depth** (verification at the
   source)
3. Expose that knowledge base via a query interface usable by an agent/LLM building agentic
   systems, e.g.:
   - *"What agent frameworks exist for tool-use orchestration, and where can I read more?"*
   - *"What approaches to agent memory have emerged recently?"*
   - *"Is there a popular framework for X? What's it called and what's its core pattern?"*

---

## Scope

**In scope:**
- LLM agents and agent frameworks
- Agentic architectures and patterns (planning, memory, tool use, multi-agent)
- New open-source frameworks and libraries in the agent space
- Relevant papers (arXiv, preprints)
- Announcements and commentary from key practitioners

**Out of scope:**
- General ML / deep learning (no vision, audio, etc.)
- LLM training and fine-tuning research (unless directly agent-related)
- Hardware, infrastructure, MLOps

---

## Architecture

### 1. Scraping & Monitoring — Hermes

Hermes runs on scheduled cron triggers and covers two parallel tracks. In both tracks, Hermes's
job is strictly **search, extract, and format — never summarize**. Hermes pushes mechanical
filtering (date ranges, categories, keywords) to each source's own API where possible, then
makes a semantic in-scope/out-of-scope judgment on what's returned. Summarization/synthesis is
WikiLLM's job, downstream.

**Research track** (validated):
- arXiv (cs.AI, cs.CL, filtered by submission date range via arXiv's API; in-scope judgment
  by Hermes; abstract stored verbatim — see `prompts/arxiv_research.md`)
- Possible future additions: Semantic Scholar, key practitioner blogs, HuggingFace papers

**Framework discovery track** (in design):
- GitHub Search API, two cadences:
  - Weekly: established/popular frameworks (sorted by stars) — with change-detection
    (compare `pushed_at` against the last scrape) to avoid re-fetching unchanged READMEs
  - Daily: newly created/updated repos with traction — catches emerging frameworks
- Full README stored verbatim (unlike arXiv abstracts, READMEs are short enough in aggregate
  that no summarization is needed even for storage)
- Possible future additions: HuggingFace new repositories, Hacker News (Show HN), Twitter/X

There will naturally be overlap between the two tracks (a new framework often has an
accompanying paper). This is acceptable — deduplication is handled at the WikiLLM ingestion
stage.

Scraped content is dropped into a flat `/sources` folder for ingestion (filenames prefixed by
source type and ID, e.g. `arxiv-<id>.md`, `github-<owner>_<repo>.md`). Source path is
configured in `.wiki-compiler.json`.

### 2. Knowledge Base — WikiLLM

**Chosen implementation: `ussumant/llm-wiki-compiler`** (Claude Code plugin).
It ingests `/sources` and builds a structured, interlinked wiki:

- **Customizable extraction schema:** `wiki/schema.md` is a natural language document the
  compiler reads before every run — defines entity types, article structure, tagging conventions,
  and cross-reference rules. This is the key reason for choosing this implementation over
  standalone CLI tools, which have hardcoded extraction prompts with no override mechanism.
- Hash-based incremental compilation — only recompiles topics whose source files changed
- Automated via `claude -p "/wiki-compile"` in cron once `.wiki-compiler.json` and `schema.md`
  are committed to the repo (one-time interactive `/wiki-init` required to bootstrap config)
- Query interface via `/wiki-query` slash command

### 3. Query Agent

Given the revised goal, the "query agent" is less a custom-built chatbot and more **direct use
of `llm-wiki-compiler`'s `context`/MCP interface** by a coding agent — i.e. an LLM working on
an agentic-systems project can query this wiki mid-task to check "does a framework like this
already exist, and what's it called / how does it broadly work / where do I read more."
A thin wrapper or prompt convention may still be useful, but building a separate agent from
scratch is likely unnecessary.

---

## What Success Looks Like

At the end of this project:

- Hermes runs on cron schedules for both tracks, reliably depositing scraped content into `/sources`
- `ussumant/llm-wiki-compiler` ingests that content and maintains an up-to-date, citation-backed wiki
- A coding agent can query the wiki (via `/wiki-query`) to get an answer like
  "yes, framework X exists, here's roughly what it does, here's where to verify current details"
- The pipeline is understood well enough to reason about how it would transfer to the
  pharmaceutical use case

---

## Open Questions

- ~~Which WikiLLM implementation to use~~ — resolved: `ussumant/llm-wiki-compiler` (Claude Code plugin with customizable `schema.md`; chosen over standalone CLI tools for extraction control)
- Framework discovery track: exact GitHub search query (topics + free-text), star thresholds
  for the "emerging" query, and the change-detection check (compare `pushed_at`)
- Whether/when to revisit ingestion depth (e.g. full PDF text for papers) if the query agent's
  use cases demand more than abstract/README-level awareness
- Gateway/cron automation so jobs run unattended (`hermes gateway install`)
- Whether a thin query-agent wrapper around `llmwiki context`/MCP is needed, or direct use
  suffices
