# Wiki Schema

This file defines the structure and conventions for this knowledge base wiki. It is generated on first compile and co-evolved between human and LLM on subsequent runs.

**Human:** You can edit this file to rename topics, merge them, add conventions, or change the article structure. The compiler will respect your changes on the next run.

**Compiler:** Read this file before classifying sources. Follow its conventions. Add new topics here when discovered. Never remove topics without human approval.

## Topics

Each source file (`github-<owner>_<repo>.md`) maps 1:1 to one entity page for that framework. No sub-feature pages for things mentioned in only one repo.

### Active Topics

| Slug | Framework Name | Status |
|------|---------------|--------|
| activepieces_activepieces | Activepieces | active |
| aden-hive_hive | Hive (OpenHive) | active |
| agentscope-ai_agentscope | AgentScope | active |
| areal-project_areal | AReaL | active |
| browser-use_browser-harness | Browser Harness | active |
| camel-ai_camel | CAMEL | active |
| camel-ai_owl | OWL (Optimized Workforce Learning) | active |
| can1357_oh-my-pi | Oh My Pi (omp) | active |
| cft0808_edict | Edict (三省六部) | active |
| e2b-dev_e2b | E2B | active |
| esengine_deepseek-reasonix | DeepSeek-Reasonix | active |
| evomap_evolver | Evolver | active |
| gitlawb_openclaude | OpenClaude | active |
| google_adk-python | Agent Development Kit (ADK) | active |
| gptme_gptme | gptme | active |
| hkuds_nanobot | nanobot | active |
| jackwener_opencli | OpenCLI | active |
| langroid_langroid | Langroid | active |
| letta-ai_letta | Letta (formerly MemGPT) | active |
| lsdefine_genericagent | GenericAgent | active |
| microsoft_agent-framework | Microsoft Agent Framework (MAF) | active |
| microsoft_autogen | AutoGen | deprecated — succeeded by microsoft_agent-framework |
| nousresearch_hermes-agent | Hermes Agent | active |
| opensandbox-group_opensandbox | OpenSandbox | active |
| othmanadi_planning-with-files | Planning with Files | active |
| panniantong_agent-reach | Agent Reach | active |
| pydantic_pydantic-ai | Pydantic AI | active |
| rightnow-ai_openfang | OpenFang | active |
| ruvnet_ruflo | Ruflo | active |
| significant-gravitas_autogpt | AutoGPT | active |
| strands-agents_harness-sdk | Strands Agents | active |
| the-pocket_pocketflow | PocketFlow | active |
| transformeroptimus_superagi | SuperAGI | low-activity — last push 2025-01-22 |
| trycua_cua | Cua | active |
| waooai_waoowaoo | waoowaoo AI Film Studio | active |
| yeachan-heo_oh-my-claudecode | oh-my-claudecode | active |
| zhayujie_cowagent | CowAgent | active |

## Concepts

Cross-cutting patterns that span 3+ topics. Interpretive, not just factual.

| Slug | Description |
|------|-------------|
| mcp-as-integration-layer | MCP has become the de facto interop protocol across 20+ frameworks — consumer and producer simultaneously |
| persistent-agent-memory | 11 frameworks implement memory, but with fundamentally different architectures: recall vs. skill vs. distillation |
| self-evolving-agents | Agents improving their own capabilities across 8 frameworks at different timescales and granularities |
| claude-code-ecosystem-gravity | Claude Code / OpenClaw is a gravitational center: 10 frameworks are forks, harnesses, skills, or migration paths |
| human-in-the-loop-as-production-primitive | HITL in 15 frameworks at 4 distinct architectural layers: tool, workflow, governance, harness |
| sandboxed-execution-as-infrastructure | Dedicated sandbox infrastructure tier has emerged: E2B, OpenSandbox, Cua + 4 embedded sandbox implementations |

## Article Structure

Each topic article follows this format (customized for this AI framework tracker):

- **Summary** [coverage] — what the framework does and its key value proposition; includes scraped_at date for time-sensitive tracking
- **Core Pattern** [coverage] — orchestration approach, key abstractions (multi-agent, workflow, memory, tool-calling, etc.)
- **Key Features** [coverage] — notable capabilities: MCP support, RAG, UI, self-hosting, etc.
- **Tech Stack** [coverage] — primary language, deployment model, notable dependencies
- **Traction** [coverage] — stars, activity level, community signals, release cadence
- **Use Cases** [coverage] — what the framework is best suited for
- **Related Frameworks** [coverage] — similar or competing frameworks with explicit differentiators
- **Sources** — backlinks to all contributing source files (required)

Coverage tags: `[coverage: high — N sources]`, `[coverage: medium — N sources]`, `[coverage: low — N sources]`

## Naming Conventions

- Topic slugs: `owner_repo` format, lowercased, matching the source filename without the `github-` prefix and `.md` extension (e.g., `nousresearch_hermes-agent`, `the-pocket_pocketflow`) — guarantees uniqueness across repos with identical names
- Source files: `github-<owner>_<repo>.md` in `sources/` — one file per repo, re-scraping overwrites (built-in dedup)
- Topic files: `{slug}.md` in `wiki/topics/`
- Concept files: `{concept-slug}.md` in `wiki/concepts/`
- Dates: YYYY-MM-DD format; use `scraped_at` from frontmatter as the source date for these GitHub sources
- Links: Obsidian `[[wikilinks]]` with relative paths from `topics/` (e.g., `[[../../sources/github-owner_repo]]`)

## Cross-Reference Rules

- Each source file → exactly one topic article (one framework entity per repo)
- Cross-cutting architectural patterns appearing in 3+ repos → concept pages in `wiki/concepts/`
- Do not create sub-feature pages for things mentioned in only one repo
- Related Frameworks section in each article should cross-reference other tracked frameworks when relevant

## Evolution Log

- 2026-06-29: Initial schema generated from 18 topics, 4 concepts. First compile.
- 2026-07-03: Full recompile with 37 topics (19 new). Topic slugs migrated to `owner_repo` format. 6 concepts updated/created: mcp-as-integration-layer (rebuilt, expanded from 11 to 22 topics), persistent-agent-memory (rebuilt, expanded to 11 topics), self-evolving-agents (rebuilt, expanded to 8 topics), claude-code-ecosystem-gravity (new), human-in-the-loop-as-production-primitive (new), sandboxed-execution-as-infrastructure (new). Previous 4 concepts (cli-coding-agent-convergence deleted — content folded into claude-code-ecosystem-gravity and self-evolving-agents which better capture the pattern).
