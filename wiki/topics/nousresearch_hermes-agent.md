---
topic: nousresearch_hermes-agent
last_compiled: 2026-07-03
sources:
  - ../../sources/github-NousResearch_hermes-agent
status: active
---

# Hermes Agent

## Summary [coverage: low — 1 source]

Scraped 2026-07-03T23:58:09Z. Hermes Agent is a self-improving personal AI agent built by Nous Research, featuring a built-in closed learning loop that creates skills from experience, improves them during use, and builds a persistent model of the user across sessions. It runs across six terminal backends (local, Docker, SSH, Singularity, Modal, Daytona) and integrates with Telegram, Discord, Slack, WhatsApp, Signal, and other messaging platforms from a single gateway process, enabling access from a $5 VPS or serverless infrastructure. With 208,686 stars it is the most-starred framework in this tracked set, reflecting extraordinary community traction since its July 2025 creation.

## Core Pattern [coverage: low — 1 source]

- Closed learning loop: agent autonomously creates skills after complex tasks, improves them during use, and nudges itself to persist knowledge; FTS5 session search with LLM summarization enables cross-session recall
- Dual entry points: full TUI terminal interface and a messaging gateway process bridging Telegram, Discord, Slack, WhatsApp, Signal, and Email into a single agent session
- Six terminal backends (local, Docker, SSH, Singularity, Modal, Daytona) enabling serverless persistence — agent environment hibernates when idle and wakes on demand
- Subagent delegation: spawns isolated subagents for parallel workstreams; Python scripts call tools via RPC to collapse multi-step pipelines into zero-context-cost turns
- Honcho dialectic user modeling for persistent user profiling across sessions
- Skills system compatible with the agentskills.io open standard

## Key Features [coverage: low — 1 source]

- 40+ tools with a configurable toolset system; Nous Portal Tool Gateway bundles web search (Firecrawl), image generation (FAL), TTS (OpenAI), and cloud browser (Browser Use) under one subscription
- Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output
- Messaging gateway: Telegram, Discord, Slack, WhatsApp, Signal, Email from a single process; voice memo transcription; cross-platform conversation continuity
- Built-in cron scheduler for unattended automations with delivery to any connected platform; natural language scheduling
- MCP integration: connect any MCP server for extended capabilities
- Model-agnostic: Nous Portal, OpenRouter, OpenAI, custom endpoints, and others; switch with `hermes model` at runtime, no code changes
- Research utilities: batch trajectory generation and trajectory compression for training tool-calling models
- Migration path from OpenClaw: `hermes claw migrate` imports settings, memories, skills, API keys, and workspace instructions
- Known bug (#23450): unconditional sending of `include: ["reasoning.encrypted_content"]` breaks non-o-series models (gpt-4o, gpt-4o-mini); o-series models also require OpenAI org verification for reasoning summaries

## Tech Stack [coverage: low — 1 source]

- Primary language: Python 3.11
- Package manager: uv (Astral); installer handles uv, Python 3.11, Node.js, ripgrep, ffmpeg, and Git automatically
- Platform support: Linux, macOS, WSL2, Termux (Android), Windows native (PowerShell one-liner)
- Deployment targets: local, Docker, SSH, Singularity, Modal (serverless), Daytona (serverless), VPS, GPU cluster
- Memory/user modeling: Honcho (plastic-labs/honcho) for dialectic user modeling
- Skills standard: agentskills.io open standard
- MIT license; built by Nous Research (nousresearch.com)

## Traction [coverage: low — 1 source]

- 208,686 stars — by far the highest star count among all 37 tracked frameworks
- Active development: pushed 2026-07-03, same day as scrape
- Created 2025-07-22 — reached this scale in approximately 11 months
- Multi-language README: Chinese, Urdu, Spanish — indicates broad international reach
- Discord community at discord.gg/NousResearch; Skills Hub at agentskills.io
- Community extensions: computer-use-linux (Linux desktop-control MCP server), HermesClaw (WeChat bridge)
- Nous Portal subscription available with 300+ models

## Use Cases [coverage: low — 1 source]

- Personal AI assistant that persists knowledge and adapts to the user's profile across sessions
- Remote agent accessible from mobile messaging apps (Telegram, WhatsApp, etc.) while running on a cloud VM or serverless backend
- Automated pipeline orchestration: scheduled daily reports, nightly backups, weekly audits via built-in cron
- Parallel research or development workstreams via subagent delegation
- Infrastructure-constrained deployments: serverless (Modal, Daytona) that cost nearly nothing when idle
- Research use: generating and compressing agent trajectories for training tool-calling models
- Migration path for OpenClaw users

## Related Frameworks [coverage: low — 1 source]

- [[letta-ai_letta]] — also built around persistent memory and self-improvement; Letta is API-platform-first for application embedding while Hermes is personal-agent-first with messaging gateway and serverless deployment
- [[lsdefine_genericagent]] — also self-evolving with skill crystallization; GenericAgent emphasizes minimal architecture (~3K lines) and token efficiency while Hermes offers a broader feature set (scheduling, multi-platform gateway, research tooling)
- [[gitlawb_openclaude]] — predecessor/related project; Hermes includes direct migration tooling (`hermes claw migrate`) from OpenClaw
- [[gptme_gptme]] — similar terminal-first personal agent with persistent memory and tool use; narrower platform reach, no messaging gateway or serverless backends
- [[microsoft_agent-framework]] — enterprise multi-agent orchestration; organization-facing where Hermes is individual-user-facing with a learning loop and personal memory

## Sources

- [[../../sources/github-NousResearch_hermes-agent]]
