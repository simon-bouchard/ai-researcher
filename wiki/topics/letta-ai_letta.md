---
topic: letta-ai_letta
last_compiled: 2026-07-03
sources:
  - ../../sources/github-letta-ai_letta
status: active
---

# Letta (formerly MemGPT)

## Summary [coverage: low — 1 source]

Scraped 2026-07-01T02:45:11Z. Letta is a platform for building stateful AI agents with advanced persistent memory that can learn and self-improve over time, originally developed as MemGPT. It offers two entry points: Letta Code, a terminal-based CLI agent for local computer tasks, and the Letta API for integrating stateful agents into applications via Python and TypeScript SDKs. The framework is model-agnostic and positions itself around memory as a first-class primitive, with agents that retain and update knowledge across sessions.

## Core Pattern [coverage: low — 1 source]

- Agents maintain explicit memory blocks (e.g. `human`, `persona`, and custom labels) that persist across all sessions as structured key-value stores injected into agent context at runtime
- Two integration modes: Letta Code (CLI, npm-based) for local terminal use; Letta API (REST + SDK) for embedding stateful agents into external applications
- Model-agnostic: model is specified at agent creation time; any provider can be used
- Supports skills and subagents composable at the CLI level for advanced task delegation and continual learning workflows
- Agent state managed server-side (hosted service or self-hosted), decoupled from the calling application

## Key Features [coverage: low — 1 source]

- Persistent memory blocks attached to each agent (human context, persona, and custom labels)
- Built-in tools: web_search, fetch_webpage; extensible tool system
- Pre-built skills and subagents bundled with Letta Code for advanced memory and continual learning
- Python SDK (`letta-client`) and TypeScript/Node.js SDK (`@letta-ai/letta-client`)
- Full REST API with reference documentation at docs.letta.com
- Model leaderboard (leaderboard.letta.com) for evaluating model performance with Letta agents; recommends Opus 4.5 and GPT-5.2 for best results
- Open source with 100+ contributors; active Discord and developer forum community

## Tech Stack [coverage: low — 1 source]

- Primary language: Python (server/SDK); TypeScript/Node.js (CLI tool and client SDK)
- CLI tool: `@letta-ai/letta-code` (npm, requires Node.js 18+)
- Python SDK: `letta-client` (pip)
- Deployment: hosted Letta API (app.letta.com) or self-hosted; agent state managed server-side
- Model support: model-agnostic; recommended models listed on leaderboard

## Traction [coverage: low — 1 source]

- 23,597 stars on GitHub
- Active development: pushed 2026-06-26, five days before scrape
- Created 2023-10-11 (as MemGPT), one of the older projects in the tracked set
- 100+ contributors worldwide
- Community channels: Discord, developer forum, Twitter/X, LinkedIn, YouTube

## Use Cases [coverage: low — 1 source]

- Building agents that must remember user preferences, context, or prior interactions across sessions
- Coding assistants with persistent memory running locally in the terminal (Letta Code)
- Applications requiring long-running, stateful agents embedded via API (customer support, personal assistants, research agents)
- Continual-learning agent pipelines where agents refine their own persona or knowledge over time
- Multi-agent workflows using subagents and skills for task decomposition

## Related Frameworks [coverage: low — 1 source]

- [[nousresearch_hermes-agent]] — also emphasizes persistent memory and cross-session learning with a closed skill-creation loop; Hermes is personal-CLI/gateway-first while Letta is API-platform-first for application embedding
- [[microsoft_autogen]] — multi-agent orchestration with group-chat patterns; stateless by default, no built-in persistent memory primitive
- [[microsoft_agent-framework]] — enterprise successor to AutoGen; production workflow orchestration without memory as a core design primitive
- [[langroid_langroid]] — Python message-passing multi-agent framework; task-based rather than memory-centric
- [[google_adk-python]] — structured agent/tool framework from Google; stateless across sessions by default

## Sources

- [[../../sources/github-letta-ai_letta]]
