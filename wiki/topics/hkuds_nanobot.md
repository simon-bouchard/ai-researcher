---
topic: hkuds_nanobot
last_compiled: 2026-07-03
sources:
  - ../../sources/github-HKUDS_nanobot
status: active
---

# nanobot

## Summary [coverage: low — 1 source]

Scraped 2026-07-03T23:58:13Z. nanobot is an open-source, ultra-lightweight personal AI agent designed for daily long-running work, emphasizing a small readable core with practical production features: a bundled browser WebUI, multi-channel chat (Telegram, Feishu, Slack, Discord, Teams, WeChat, Email), MCP support, persistent memory, model routing with fallback models, automation scheduling, and flexible deployment. Launched February 2026 by HKUDS (Xubin Ren at Hong Kong University), it reached 44,988 stars by July 2026, reflecting rapid adoption. v0.2.2 ("Durability Release") focused on sturdier long-running agent behavior including segmented WebUI transcripts, Python SDK runtime controls, and stronger session/provider reliability.

## Core Pattern [coverage: low — 1 source]

- Small central agent loop: messages in from any channel, LLM decides on tool use, memory/skills pulled in as context rather than a heavy orchestration layer
- `/goal` command: sustained long-term objectives held across conversation turns
- Memory: two-stage Dream memory system with token-based management and auto-compact on idle
- Automations: cron-based scheduling, session-bound automations, natural-language reminders
- Model presets with fallback models for reliability; `/model` switching at runtime
- Sub-agents supported in CLI mode
- OpenAI-compatible API exposed for integration with external tools

## Key Features [coverage: low — 1 source]

- Bundled browser WebUI (ships inside the published wheel, no separate build step)
- Multi-channel: Telegram, Feishu, Discord, Slack, Teams, WeChat, WeCom, QQ, Matrix, Email, Signal, WhatsApp
- MCP (Model Context Protocol) support with multiple servers, MCP presets, reconnect handling
- Python SDK with runtime controls and composable agent lifecycle hooks
- Langfuse observability integration
- Image generation (multi-provider), speech-to-text (multiple providers), voice input
- CLI Apps and skill registry (ClawHub)
- Docker and Linux service deployment; macOS LaunchAgent; Windows PowerShell install script
- Multilingual documentation (10+ languages); nanobot.wiki documentation site

## Tech Stack [coverage: low — 1 source]

- Language: Python 3.11+
- Package: `nanobot-ai` on PyPI
- Install: one-command shell/PowerShell script, uv, pip, or source
- Native SDKs: replaced litellm with native `openai` + `anthropic` SDKs (March 2026)
- WebUI: Vite-based React frontend bundled into the wheel
- Gateway: WebSocket on port 8765; health endpoint on 18790
- Config: `~/.nanobot/config.json`; provider cookbook for copy-paste setup

## Traction [coverage: low — 1 source]

- 44,988 stars
- Created 2026-02-01; pushed 2026-07-03 — approximately 5 months old at scrape time, extremely rapid growth
- Near-daily releases; v0.2.2 at scrape time
- Open source partners: Kimi (Moonshot AI), MiniMax
- Communities: Discord, WeChat group, Feishu group; Twitter @nanobot_project
- Started as a personal project by Xubin Ren; community contributors active

## Use Cases [coverage: low — 1 source]

- Personal AI assistant reachable through existing chat apps (Telegram, Slack, WeChat) without leaving them
- Long-running autonomous agent tasks (market analysis, coding, scheduling) with `/goal`-based objectives
- Self-hosted alternative to commercial AI assistants with full provider and data control
- Multi-modal workflows: text, images, voice, video across chat channels
- Teams wanting a lightweight deployable agent with MCP extensibility

## Related Frameworks [coverage: low — 1 source]

- [[gptme_gptme]] — also lightweight and terminal-first; gptme emphasizes the developer autonomous-agent scaffold, nanobot emphasizes chat-channel reach and WebUI
- [[gitlawb_openclaude]] — terminal coding agent; nanobot is more of a general-purpose personal assistant with broader channel integration
- [[letta-ai_letta]] — persistent memory platform; nanobot achieves memory via the Dream system without a separate managed service
- [[zhayujie_cowagent]] — another personal assistant bot with chat-channel integration; nanobot is more general-purpose and heavily maintained
- [[microsoft_autogen]] — enterprise multi-agent orchestration; nanobot targets individual/small-team self-hosted use with a minimal core

## Sources

- [[../../sources/github-HKUDS_nanobot]]
