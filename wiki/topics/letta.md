---
topic: letta
last_compiled: 2026-06-29
source_count: 1
status: active
---

# Letta (formerly MemGPT)

## Summary [coverage: high — 1 source]

Letta is an open-source platform for building stateful AI agents with advanced, persistent memory that can learn and self-improve over time. Originally released as MemGPT (October 2023), it rebranded to Letta and expanded from a research prototype into a full agent platform. It exposes two primary entry points: a local CLI tool (Letta Code) for terminal-based agentic tasks, and a REST API with Python and TypeScript SDKs for embedding stateful agents in applications. The core value proposition is persistent, structured memory — agents remember context across sessions and can update their own internal state. *Source data scraped 2026-06-16.*

## Core Pattern [coverage: high — 1 source]

Letta's central abstraction is the **stateful agent**: each agent carries typed **memory blocks** (e.g. `human` and `persona` labels) that persist across sessions and can be read and rewritten by the agent itself. This gives agents a continuous identity and accumulating knowledge rather than a blank context window on every invocation.

Orchestration supports **multi-agent composition**: Letta Code exposes a **skills** and **subagents** system, where pre-built skills (discrete capabilities) and subagents (delegated agents) can be composed at the CLI level. The API layer is model-agnostic — the agent's model is specified at creation time and can be swapped freely; the platform recommends Opus 4.5 and GPT-5.2 for highest performance and publishes a public model leaderboard (`leaderboard.letta.com`).

Tool-calling is a first-class primitive: agents are created with named tools (`web_search`, `fetch_webpage`, and others) declared at instantiation, and can invoke them during message handling.

## Key Features [coverage: high — 1 source]

- **Persistent memory blocks:** Structured key/value memory (`human`, `persona`, and custom labels) stored server-side, writable by the agent — the primary differentiator from stateless frameworks.
- **Letta Code CLI:** npm-installable terminal agent (`@letta-ai/letta-code`) that runs a memory-backed agent locally; supports coding assistance, skills, and subagents out of the box.
- **Full-featured Agents API:** REST API plus official Python (`letta-client`) and TypeScript (`@letta-ai/letta-client`) SDKs with comprehensive API reference documentation.
- **Model leaderboard:** Public leaderboard ranking LLMs by Letta-specific performance (`leaderboard.letta.com`), giving users an opinionated guide for model selection.
- **Hosted and self-hosted:** Managed cloud endpoint available at `app.letta.com` (API key required); the OSS repo supports self-hosted deployment.
- **Built-in tools:** `web_search` and `fetch_webpage` available out of the box; tool list is extensible at agent creation time.
- **Skills and subagents:** Composable capability units and delegated sub-agents in Letta Code, with pre-built bundles for memory and continual learning.

## Tech Stack [coverage: medium — 1 source]

- **Primary language:** Python (server/core); TypeScript/Node.js for the Letta Code CLI and TS SDK.
- **Runtime requirement for CLI:** Node.js 18+ (for `@letta-ai/letta-code`).
- **SDKs:** `letta-client` (pip) and `@letta-ai/letta-client` (npm).
- **Deployment model:** Hosted SaaS (`app.letta.com`) or self-hosted OSS; the README does not detail infrastructure dependencies (database, vector store) but persistent memory implies a server-side store.
- **Model provider:** Model-agnostic; API-level model selection at agent creation (`openai/gpt-5.2`, Anthropic Opus 4.5, etc.).

## Traction [coverage: high — 1 source]

- **23,352 GitHub stars** — strong adoption signal for a framework in this space.
- **Repository age:** Created October 2023 (originally as MemGPT); over two and a half years of active development.
- **Last pushed:** 2026-05-14 — actively maintained at time of scraping.
- **Contributor base:** Over 100 contributors from around the world, indicating a genuine open-source community rather than a solo project.
- **Community channels:** Discord (`discord.gg/letta`), dedicated developer forum (`forum.letta.com`), active presence on Twitter/X, LinkedIn, and YouTube.

## Use Cases [coverage: medium — 1 source]

- **Long-running assistants:** Applications where agents must remember users, preferences, and prior interactions across many sessions (CRM bots, personal assistants, support agents).
- **Continual-learning agents:** Scenarios where the agent should update its own knowledge or persona over time — e.g. coaching tools, evolving research assistants.
- **Terminal coding agents:** Letta Code positions the framework for software development workflows, comparable to Cursor/Claude Code but with persistent memory baked in.
- **Application-embedded agents:** Embedding stateful agents into SaaS products via the Agents API — the SDK-first design targets production integrations.
- **Multi-agent pipelines:** Composition of specialist subagents via the skills/subagents system for complex task delegation.

## Related Frameworks [coverage: low — 1 source]

- **LangChain / LangGraph:** General orchestration frameworks with memory modules, but memory is an add-on rather than the core primitive; Letta treats memory as the foundational design center.
- **CrewAI:** Multi-agent role-based orchestration; shares the multi-agent composition pattern but lacks Letta's persistent per-agent memory model.
- **AutoGen (Microsoft):** Multi-agent conversation framework; similarly supports agent composition but memory persistence is not its primary value proposition.
- **OpenAI Assistants API:** Closest hosted analogue — stateful threads and built-in retrieval — but proprietary and locked to OpenAI models, whereas Letta is model-agnostic and self-hostable.
- **Mem0:** Dedicated memory layer that can be added to other frameworks; Letta integrates memory directly into the agent runtime rather than as a separate service.

## Sources [coverage: high — 1 source]

- [[../../sources/github-letta-ai_letta]]
