# Wiki Schema

This file defines the structure and conventions for this knowledge base wiki. It is generated on first compile and co-evolved between human and LLM on subsequent runs.

**Human:** You can edit this file to rename topics, merge them, add conventions, or change the article structure. The compiler will respect your changes on the next run.

**Compiler:** Read this file before classifying sources. Follow its conventions. Add new topics here when discovered. Never remove topics without human approval.

## Topics

Each source file (`github-<owner>_<repo>.md`) maps 1:1 to one entity page for that framework. No sub-feature pages for things mentioned in only one repo.

- `activepieces`: Open-source workflow automation platform (Zapier alternative) with MCP-native integration; every piece auto-publishes as an MCP server
- `agent-reach`: Capability layer (not a framework) that extends Claude Code and other AI agents with browser, computer, and web tool access across 12+ platforms
- `agentscope`: Alibaba-backed production-grade Python agent framework with async streaming, middleware system, and FastAPI multi-tenant service; v2.0 May 2026
- `areal`: RL training infrastructure for LLM reasoning/agentic models at scale (Tsinghua IIIS + Ant Group); produces agents rather than operating them
- `autogen`: Microsoft Research multi-agent framework (maintenance mode as of 2026); official successor is Microsoft Agent Framework (MAF)
- `cowagent`: High-traction Python agent harness (formerly chatgpt-on-wechat) with three-tier memory, Deep Dream distillation, self-evolution loop, and 12-channel support
- `deepseek-reasonix`: DeepSeek-native terminal coding agent (Go rewrite at v1.0); differentiates on prefix-cache stability and zero-dependency static binary
- `evolver`: GEP-powered prompt-evolution engine for AI agents; evolves only prompts (not code), ships hooks for 6 runtimes; source-available license transition in progress
- `genericagent`: Minimal self-evolving agent with 5-layer memory (L0-L4), real-browser control via TMWebdriver, and skill crystallization from task experience
- `gptme`: Local-first provider-agnostic terminal agent CLI (launched Spring 2023); 17 tool categories, MCP auto-discovery, ACP IDE integration, autonomous Bob agent
- `harness-sdk`: Strands Agents Python+TypeScript SDK with WASM bridge for cross-language interop; Amazon Bedrock default, interceptable agent loop with tracing/guardrails
- `hermes-agent`: High-traction (194k stars) terminal agent with closed learning loop: FTS5 memory, autonomous skill creation, Honcho user modeling, 6 terminal backends
- `langroid`: CMU/UW-Madison research-origin Python framework built on Actor-model multi-agent programming; strong RAG/DocChatAgent and SQL/database agent support
- `letta`: MemGPT successor focused on persistent stateful agents; memory-block abstraction with self-editing, Agents API, hosted + self-hosted options
- `nanobot`: High-traction (44k stars) personal coding + automation agent with Dream memory, `/goal` sustained-objective mode, 15+ chat channels, multi-provider routing
- `openclaude`: Community fork of Claude Code with 13+ provider backends, headless gRPC mode, named sub-agent routing for cost optimization
- `opencli`: Browser-automation CLI with 100+ site adapters; exposes Chrome DevTools Protocol as CLI subcommands for AI agents using the user's real logged-in Chrome profile
- `pocketflow`: Minimalist 100-line LLM framework using graph as core primitive; multi-language ports, 30+ cookbook examples, MCP and A2A protocol support

## Concepts

Cross-cutting patterns that span 3+ topics. Interpretive, not just factual.

- `mcp-as-integration-layer`: MCP (Model Context Protocol) has become the de facto interoperability standard across 11+ frameworks independently — not by mandate but by network effects — connects [activepieces, gptme, autogen, langroid, cowagent, pocketflow, harness-sdk, deepseek-reasonix, openclaude, agentscope, nanobot]
- `persistent-agent-memory`: Five frameworks treat agent memory as a core architectural primitive with distinct models (self-editing blocks, distillation loops, FTS5 search, tiered layers) — connects [letta, cowagent, genericagent, nanobot, hermes-agent]
- `self-evolving-agents`: Four frameworks build explicit self-improvement loops where agents write, validate, and reuse skills from their own execution experience — connects [evolver, cowagent, genericagent, hermes-agent]
- `cli-coding-agent-convergence`: Four terminal coding agents (all responding to Claude Code/Codex CLI) competing on second-order differentiation: memory, cache optimization, longevity, and provider routing — connects [hermes-agent, gptme, openclaude, deepseek-reasonix]

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

- Topic slugs: lowercase-kebab-case matching the repo name from `topic_hints` (e.g., `hermes-agent`, `pocketflow`)
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
