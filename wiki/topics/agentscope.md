---
topic: agentscope
last_compiled: 2026-06-29
source_count: 1
status: active
---

# AgentScope

## Summary [coverage: high — 1 source]

AgentScope is a production-ready Python agent framework developed by Alibaba (agentscope-ai), with the stated goal of letting developers "build and run agents you can see, understand and trust." Version 2.0 (released May 2026) reoriented the framework toward increasingly autonomous LLMs by leaning into model-native reasoning and tool use rather than imposing rigid orchestration. The design philosophy explicitly avoids constraining agents with strict prompts or opinionated pipelines, instead providing composable infrastructure (event bus, permission system, sandboxed workspaces, middleware hooks) that scales from a single-agent prototype to a multi-tenant production service. The framework has two peer-reviewed publications backing it (arXiv 2402.14034, 2508.16279).

*Source scraped: 2026-06-16T03:10:24Z.*

## Core Pattern [coverage: high — 1 source]

AgentScope's central abstraction is the `Agent` class, which combines a model backend, a `Toolkit`, and an event-driven reasoning-acting loop. The loop exposes typed events (`REPLY_START`, `MODEL_CALL_START`, `TEXT_BLOCK_START`, `TEXT_BLOCK_DELTA`, `TEXT_BLOCK_END`, etc.) via an async streaming API (`agent.reply_stream()`), making it straightforward to pipe agent output directly to a frontend or logging layer without polling.

Multi-agent coordination is handled through an **Agent Team** pattern: a leader agent spawns worker agents and directs them through built-in team tools. The leader can decompose complex tasks into a tracked plan and update it as execution proceeds. Long-running tools can be offloaded to the background; their results wake the agent when ready.

An **Extensible Middleware System** provides composable hooks into the reasoning-acting loop, allowing custom pre/post processing without forking the core agent logic. The framework is designed around model-native reasoning rather than hard-coded control flow, so orchestration emerges from the model's own tool-use decisions rather than from graph edges or state machines.

## Key Features [coverage: high — 1 source]

- **Event System:** A unified event bus connects the agent loop to the frontend and enables human-in-the-loop interrupts at any point in execution.
- **Permission System:** Fine-grained, configurable control over which tools and resources an agent can access. Supports a "bypass mode" for fully autonomous end-to-end runs without tool-call confirmation pauses.
- **Multi-tenancy and Multi-session Service:** FastAPI-based production service with strict isolation across tenants and sessions. An `Agent Service` example ships with the repo.
- **Agent Team:** A leader agent spawns and coordinates worker agents via built-in team tools; shipped as of June 2026.
- **Workspace / Sandbox Support:** Tools and code run in isolated environments. Three backends supported out of the box: local process, Docker container, and E2B cloud sandbox.
- **Background Task Offloading:** Long-running tool calls move to the background; the agent resumes when the result arrives.
- **Pre-built Web UI:** A `pnpm`-based frontend in `examples/web_ui` connects to the FastAPI backend, with animated demos for task planning, permission control, team coordination, and background offloading.
- **MCP support:** Listed as an explicit topic tag (`mcp`), indicating Model Context Protocol integration.
- **Multi-modal support:** Flagged in repo topics (`multi-modal`), though the README does not elaborate beyond the topic tag.
- **Built-in file-system toolset:** `Bash`, `Grep`, `Glob`, `Read`, `Write`, `Edit` ship as first-class `Toolkit` tools.

## Tech Stack [coverage: high — 1 source]

- **Primary language:** Python 3.11+
- **Deployment model:** Self-hosted; FastAPI service backend for production multi-tenant deployments
- **Frontend:** pnpm/Node.js web UI (separate process, connects to FastAPI backend)
- **Model integrations:** DashScope (Qwen models) shown in quickstart; the credential/model abstraction layer implies support for additional providers
- **Sandbox backends:** Local, Docker, E2B
- **Async runtime:** `asyncio` (agent loop is fully async)
- **License:** Apache 2.0
- **Package distribution:** PyPI (`pip install agentscope` / `uv pip install agentscope`); also installable from source

## Traction [coverage: high — 1 source]

- **Stars:** 26,872 — places AgentScope among the top-tier agent frameworks by GitHub star count
- **Activity:** Repository pushed as recently as 2026-06-15 (one day before scrape), indicating active development
- **Age:** Created 2024-01-12; approximately 2.5 years old at time of scrape, with a major v2.0 release in May 2026
- **Publications:** Two arXiv papers (2402.14034 for the original multi-agent platform; 2508.16279 for v1.0 developer-centric framework); a large named contributor list signals institutional backing from Alibaba DAMO Academy
- **Community:** Discord server and DingTalk group; bilingual documentation (English and Chinese)
- **Trendshift badge** embedded in README, indicating sustained trending status on GitHub

## Use Cases [coverage: medium — 1 source]

- **Production agentic services:** Multi-tenant, multi-session deployments with user isolation — suitable for SaaS agent products
- **Task automation with long-running tools:** Background offloading pattern handles slow tools (web scraping, code execution, file processing) without blocking the conversation loop
- **Human-in-the-loop workflows:** Event system and permission controls make it practical to build pipelines that pause for human approval at configurable checkpoints
- **Code and filesystem agents:** Built-in Bash/Grep/Glob/Read/Write/Edit toolkit maps directly to software engineering assistant use cases
- **Research prototyping:** Lightweight single-agent path (`Agent` + `Toolkit`) with minimal boilerplate; academic use is supported by the published papers and citation block in the README
- **Multi-agent coordination:** Agent Team pattern suits orchestrator-worker architectures (e.g., a planner delegating to specialist subagents)

## Related Frameworks [coverage: medium — 1 source]

- **LangGraph / LangChain:** Graph-based orchestration with explicit state machines; AgentScope favors model-native reasoning over graph-defined control flow, trading explicitness for flexibility
- **AutoGen (Microsoft):** Also targets multi-agent conversation patterns; AgentScope adds production concerns (multi-tenancy, permission system, sandboxed workspaces) that AutoGen does not emphasize
- **CrewAI:** Role-based multi-agent orchestration; AgentScope's team pattern is similar but more infrastructure-focused (FastAPI service, event bus, sandboxes)
- **OpenHands:** Heavy emphasis on sandboxed code execution (Docker/E2B); AgentScope overlaps on sandbox backends but targets broader agent service deployment rather than a standalone coding agent
- **Agno / Phidata:** Also Python-native agent frameworks with multi-agent support; AgentScope distinguishes itself with the event system, formal permission controls, and multi-tenant service architecture

## Sources [coverage: high — 1 source]

- [[../../sources/github-agentscope-ai_agentscope]]
