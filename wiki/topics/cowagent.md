---
topic: CowAgent
last_compiled: 2026-06-29
source_count: 1
status: active
---

# CowAgent

## Summary [coverage: high — 1 source]

CowAgent (formerly chatgpt-on-wechat) is an open-source "Agent Harness" framework — a self-hosted AI assistant that proactively plans multi-step tasks, executes them via tools and skills, and self-evolves through persistent memory and a personal knowledge base. Its core value proposition is combining enterprise-grade agent capabilities (planning, memory, MCP, multi-channel delivery) with a one-line install and a unified web console, making it deployable by individual developers on a personal machine or server with no infrastructure overhead.

Source scraped at: 2026-06-16T03:25:12Z. Last pushed: 2026-06-15.

## Core Pattern [coverage: high — 1 source]

CowAgent implements a layered **Agent Harness** architecture: inbound messages arrive through any connected **Channel** (web, IM platforms), are processed by the **Agent Core**, which plans and reasons over memory, knowledge, and available tools and skills, and the response is delivered back through the originating channel.

Key orchestration abstractions:

- **Planning loop** — decomposes complex goals into sub-tasks and iterates over tools until the goal is satisfied; not a static DAG but a dynamic loop
- **Three-tier memory** — conversation context (short-term) → daily memory (mid-term) → MEMORY.md long-term core; a nightly "Deep Dream" distillation pass consolidates scattered memories into refined long-term entries and a narrative journal
- **Personal knowledge base** — distinct from memory: structures topic-organized knowledge as an auto-curated Markdown wiki with a visual knowledge-graph view, automatically updated from conversations
- **Self-Evolution** — background process that reviews past conversations to improve skills, follow up on unfinished tasks, and consolidate memory/knowledge without manual prompting
- **Skills** — higher-level workflows defined by a manifest that compose multiple atomic tools; can be authored conversationally via a built-in `skill-creator`
- **Tools** — atomic capabilities (file I/O, terminal, browser, web search, memory retrieval, scheduler, vision, MCP servers); the agent selects and sequences them during planning

## Key Features [coverage: high — 1 source]

- **MCP support** — native Model Context Protocol integration via a single `mcp.json`; supports stdio and SSE transports, hot reload, concurrent MCP calls, and Streamable HTTP (added v2.1.0/v2.1.1)
- **Skill Hub** — open marketplace at skills.cowagent.ai; one-click install from Hub, GitHub, ClawHub, or URL; conversational skill authoring via `skill-creator`
- **Multi-channel** — single agent instance serves Web console, Telegram, Discord, Slack, WeChat, Feishu/Lark, DingTalk, WeCom (bot and app), QQ, WeChat Official Account, and WeChat Customer Service in parallel
- **Multi-model** — Claude, OpenAI (GPT + o-series), Gemini, DeepSeek, Qwen, GLM, Doubao, Kimi, MiniMax, ERNIE, MiMo, and custom/local models; each modality (chat, vision, image gen, ASR, TTS, embeddings) can route to a different provider; swap providers from the web console without file editing
- **Multimodal** — text, image, voice, and file handling across recognition, generation, and delivery
- **Web console** — built-in UI at `localhost:9899`; manages models, channels, skills, memory, knowledge, and multi-session chat
- **Browser automation** — built-in browser tool with persistent sessions; `cow install-browser` for headless Chromium
- **Self-hosting** — one-line installer (Linux/macOS/Windows PowerShell) and Docker Compose; `cow` CLI for service management and upgrades
- **Enterprise tier** — LinkAI managed hosting, team workspaces, RBAC, audit logs, private deployment

## Tech Stack [coverage: high — 1 source]

- **Primary language:** Python (Python 3.13 supported as of v2.1.1)
- **Deployment:** local process, Docker Compose, or server; `cow` CLI wrapper for service lifecycle
- **Web console:** bundled, served on port 9899; no external frontend dependency required for self-hosting
- **MCP transports:** stdio, SSE, Streamable HTTP
- **Notable integrations:** Model Context Protocol ecosystem, Cow Skill Hub, LinkAI platform (managed hosting / enterprise)
- **License:** MIT

## Traction [coverage: high — 1 source]

- **45,332 stars** on GitHub — high-adoption project
- Trendshift-tracked repository (trending badge in README)
- Active release cadence: 8 releases between 2026-02-03 (v2.0.0) and 2026-06-09 (v2.1.1), roughly one release every 2-3 weeks
- Multi-language documentation: English, Chinese (中文), Japanese (日本語)
- Active community: WeChat community group, GitHub issues
- Project originated in 2022-08-07 as `chatgpt-on-wechat`; formally renamed to CowAgent at v2.0.0 (February 2026) with the pivot to a full agent harness
- Enterprise commercial track via LinkAI (sales@simple-future.tech)

## Use Cases [coverage: medium — 1 source]

- **Personal AI assistant** — long-running, self-hosted agent that learns from daily use through memory evolution and knowledge curation; suited to individuals who want a persistent, personalized assistant without cloud lock-in
- **IM platform bots** — deployment as an AI assistant on WeChat, Feishu, DingTalk, WeCom, QQ, Telegram, Discord, or Slack; strong fit for Chinese enterprise IM ecosystems
- **Automated task execution** — multi-step workflows combining browser, terminal, file I/O, and web search; recurring task scheduling via built-in scheduler tool
- **Skill-based automation** — custom workflows built as installable skills; teams can publish and share skills via Cow Skill Hub
- **Enterprise AI assistant** — team deployments via LinkAI with RBAC, audit logs, and managed hosting
- **Developer experimentation** — lightweight enough for a personal laptop; MCP integration makes it a testbed for the MCP ecosystem

## Related Frameworks [coverage: medium — 1 source]

- **AgentMesh** (MinimalFuture/AgentMesh) — listed as a related project; multi-agent framework oriented toward team collaboration on complex problems; CowAgent is single-agent-centric with channel multiplexing, while AgentMesh focuses on inter-agent coordination
- **bot-on-anything** (zhayujie/bot-on-anything) — earlier lightweight LLM-to-channel bridge by the same author; CowAgent supersedes it for agent use cases but bot-on-anything remains simpler for pure chatbot deployments
- **OpenHands / Devin-style coding agents** — CowAgent has terminal and browser tools but is general-purpose rather than coding-specialized; less suited to long autonomous coding sessions
- **n8n / Flowise** — workflow automation platforms with visual builders; CowAgent trades the visual workflow editor for conversational skill authoring and a stronger memory/evolution model
- **AutoGen / CrewAI** — multi-agent orchestration frameworks; CowAgent is single-agent with rich memory and channel delivery rather than a multi-agent coordination layer (though AgentMesh fills that role in the same ecosystem)

## Sources [coverage: high — 1 source]

- [[../../sources/github-zhayujie_CowAgent]]
