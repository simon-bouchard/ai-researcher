---
topic: agentscope-ai_agentscope
last_compiled: 2026-07-03
sources:
  - ../../sources/github-agentscope-ai_agentscope
status: active
---

# AgentScope

## Summary [coverage: low — 1 source]

Scraped 2026-07-03T23:58:05Z. AgentScope is a production-ready Python agent framework designed to build agents that are observable, understandable, and trustworthy. Version 2.0, released May 2026, centers on a design philosophy of leveraging model reasoning and tool-use abilities rather than constraining agents with strict prompts and opinionated orchestrations. It provides essential abstractions for serving agents at scale, including multi-tenancy, multi-session support, fine-grained permission control, and workspace sandboxing.

## Core Pattern [coverage: low — 1 source]

- **Event-driven loop:** A unified event bus streams typed events (reply start, model call, text delta, etc.) to frontends and supports human-in-the-loop interruption at any point.
- **ReAct-style agents with async streaming:** Agents expose a `reply_stream` async generator, decoupling the reasoning-acting loop from UI rendering.
- **Middleware system:** Composable hooks wrap the agent's reasoning-acting loop, enabling custom pre/post processing without forking core logic.
- **Agent teams:** A leader agent can spawn worker agents and coordinate them through built-in team tools, supporting hierarchical multi-agent workflows.
- **Background task offloading:** Long-running tools can be moved to the background; their results wake the agent asynchronously to resume the conversation.

## Key Features [coverage: low — 1 source]

- Fine-grained permission system for controlling tool and resource access, with bypass mode for unattended runs.
- Workspace/sandbox support with backends for local execution, Docker, and E2B.
- Multi-tenancy and multi-session agent service built on FastAPI, with pre-built web UI.
- Distributed RAG service with multi-tenancy and multi-session support (added June 2026).
- Agentic memory and long-term memory via Mem0 integration (added June 2026).
- MCP support listed as a topic tag, enabling tool interoperability.
- Built-in toolkit of file-system tools (Bash, Grep, Glob, Read, Write, Edit).
- Bilingual documentation (English and Chinese); Discord and DingTalk community channels.
- Apache 2.0 license; backed by academic publications (arxiv:2402.14034, arxiv:2508.16279).

## Tech Stack [coverage: low — 1 source]

- **Language:** Python 3.11+
- **Serving layer:** FastAPI (agent service backend)
- **Frontend:** pnpm / Node.js web UI
- **Key integrations:** DashScope/Qwen models, E2B sandbox, Mem0, MCP
- **Install:** PyPI (`agentscope`) or editable source install via uv/pip

## Traction [coverage: low — 1 source]

- **Stars:** 27,444
- **Last push:** 2026-07-03
- **Created:** 2024-01-12
- Active Trendshift badge present in README, indicating sustained trending activity.
- Community on Discord and DingTalk (QR code provided).
- Two arxiv papers; large contributor graph (999+ contributors displayed).

## Use Cases [coverage: low — 1 source]

- Production agent services requiring multi-tenant, multi-session isolation.
- Coding and file-system automation agents (built-in shell/file toolkit).
- Long-running background task agents where human-in-the-loop checkpoints are needed.
- Multi-agent team coordination with a hierarchical leader/worker pattern.
- RAG-augmented agents at scale with distributed retrieval backends.
- Applications requiring fine-grained permission enforcement over tool calls.

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — also multi-agent and async, but more opinionated about conversation topology; AgentScope emphasizes production serving and permission control.
- [[camel-ai_camel]] — role-playing multi-agent focus; AgentScope broader with production-grade serving and sandbox support.
- [[google_adk-python]] — Google's agent SDK with similar tool-use focus; AgentScope adds multi-tenancy service layer and permission system out of the box.
- [[letta-ai_letta]] — stateful/memory-first agent platform; AgentScope adds multi-session service infrastructure and sandbox backends.

## Sources

- [[../../sources/github-agentscope-ai_agentscope]]
