---
topic: zhayujie_cowagent
last_compiled: 2026-07-03
sources:
  - ../../sources/github-zhayujie_CowAgent
status: active
---

# CowAgent

## Summary [coverage: low — 1 source]

Scraped 2026-07-03T23:58:11Z. CowAgent (formerly chatgpt-on-wechat) is an open-source "super AI assistant" and Agent Harness implementation that proactively plans multi-step tasks, controls computers and external services, builds long-term memory and a personal knowledge base, and self-evolves by reviewing its own conversations. It is designed to be lightweight, one-line installable, and 24/7 deployable across personal computers or servers, with support for all major LLM providers and a wide range of messaging channels including WeChat, Telegram, Slack, and Discord. With 45 774 stars and active releases through mid-2026, it is the highest-starred project in the tracked set.

## Core Pattern [coverage: low — 1 source]

- Agent Harness architecture: messages flow in through pluggable Channels (web, IM platforms) to a central Agent Core that plans and reasons over memory, knowledge, tools, and skills before responding via the originating channel; all layers decoupled
- Task planning: decomposes complex goals into steps and loops over tools until the goal is reached, rather than producing a single-shot response
- Three-tier memory: conversation context (short-term) → daily memory (mid-term) → MEMORY.md (long-term); a nightly "Deep Dream" distillation pass refines scattered memories into long-term entries
- Skills: higher-level workflows composed from atomic tools; installable from Skill Hub, GitHub, or authored conversationally via a built-in `skill-creator`
- Self-Evolution: automatically reviews past conversations to improve skills, follow up on unfinished tasks, and consolidate memory and knowledge without manual intervention

## Key Features [coverage: low — 1 source]

- One-line installer for Linux, macOS, Windows, and Docker; unified Web console at `localhost:9899`
- Three-tier long-term memory with Deep Dream nightly distillation and hybrid keyword + vector retrieval
- Auto-curated personal knowledge base organised by topic, with interactive knowledge-graph view in the Web console
- Built-in tool suite: file I/O, terminal (`bash`), browser automation, scheduler, web search, web fetch, vision, memory retrieval, and more
- Native MCP (Model Context Protocol) integration via `mcp.json`; supports stdio and SSE transports with hot reload
- Open Skill Hub marketplace with one-click install; conversational skill authoring via `skill-creator`
- Multi-channel support: Web, WeChat, Feishu/Lark, DingTalk, WeCom, QQ, Telegram, Slack, Discord, WeChat Official Account
- Multimodal: text, images, voice, and file handling across recognition, generation, and delivery
- Provider-agnostic: Claude, GPT, Gemini, DeepSeek, Qwen, GLM, Kimi, MiniMax, Doubao, and others; swap providers from the Web console with one click
- Enterprise managed hosting via LinkAI with workspaces, RBAC, and audit logs

## Tech Stack [coverage: low — 1 source]

- Primary language: Python (supports Python 3.13+)
- Deployment: local (Linux/macOS/Windows), Docker; Web console on port 9899
- Key dependencies: MCP protocol (stdio/SSE), browser automation tooling, vector retrieval for memory
- CLI: `cow` CLI for service control, updates, and skill management
- Enterprise layer: LinkAI hosted platform (optional)
- MIT licence

## Traction [coverage: low — 1 source]

- 45 774 stars — highest in the full tracked set
- Created 2022-08-07 (originally as chatgpt-on-wechat); last pushed 2026-07-03 — consistently active for nearly four years
- Active release cadence: v2.1.2 shipped 2026-06-18; major v2.0.0 relaunch in February 2026 introduced the current agent/memory/skills architecture
- WeChat community group; Trendshift trending badge
- Related open-source ecosystem: Cow Skill Hub, bot-on-anything, AgentMesh (multi-agent framework)

## Use Cases [coverage: low — 1 source]

- Personal AI assistant running 24/7 on a home server or cloud VM, accessible via WeChat, Telegram, or web
- Automated task execution with planning: research, scheduling, file management, web browsing
- Long-term personal knowledge management and memory across conversations
- IM-platform chatbot deployment for enterprises (WeChat Official Account, DingTalk, Feishu, WeCom)
- Building and distributing reusable AI skills via Skill Hub for the broader agent ecosystem
- Self-evolving workflow automation where the agent improves its own behaviour over time

## Related Frameworks [coverage: low — 1 source]

- [[letta-ai_letta]] — also focuses on long-term agent memory and persistence, but targets developer-built stateful agents rather than a self-hosted personal assistant
- [[microsoft_autogen]] — multi-agent orchestration framework; CowAgent is a single-agent harness with broader channel and memory focus rather than multi-agent collaboration
- [[significant-gravitas_autogpt]] — similar self-directed task-planning agent with memory; CowAgent emphasises IM channel integration and a polished end-user Web console
- [[strands-agents_harness-sdk]] — also self-describes as an "Agent Harness" but is a developer SDK for building agents, not a complete self-hostable assistant platform
- [[camel-ai_camel]] — multi-agent coordination; CowAgent instead wraps a single agent in a rich channel/memory/skills harness for personal or enterprise deployment

## Sources

- [[../../sources/github-zhayujie_CowAgent]]
