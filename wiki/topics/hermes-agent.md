---
topic: hermes-agent
last_compiled: 2026-06-29
source_count: 1
status: active
---

# Hermes Agent

## Summary [coverage: high — 1 source]

Hermes Agent (NousResearch/hermes-agent) is a self-improving, model-agnostic AI agent built by Nous Research. Its core value proposition is a closed learning loop: it creates reusable skills from experience, improves those skills during use, maintains persistent memory across sessions, and builds an evolving model of the user over time. The agent runs entirely on self-hosted infrastructure — from a $5 VPS to a GPU cluster to serverless platforms — and reaches the user through a unified gateway across Telegram, Discord, Slack, WhatsApp, Signal, and a full terminal UI.

Source scraped at: **2026-06-16T03:25:10Z** (pushed 2026-06-16; created 2025-07-22).

## Core Pattern [coverage: high — 1 source]

Hermes is built around a **persistent single-agent loop with a built-in learning system**, rather than a declarative workflow graph or a supervisor/worker multi-agent topology:

- **Skills system (procedural memory):** After completing complex tasks, the agent autonomously creates named, reusable skills. Skills self-improve during subsequent use. User-created skills are shareable via the agentskills.io open standard.
- **Memory and user modeling:** Agent-curated MEMORY.md with periodic nudges to persist knowledge. FTS5 full-text session search with LLM summarization for cross-session recall. Honcho dialectic user modeling for a deepening per-user profile.
- **Subagent delegation:** Spawns isolated subagents for parallel workstreams. Supports Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns.
- **Cron scheduler:** Natural-language scheduled automations with delivery to any connected messaging platform (Telegram, Discord, etc.).
- **Gateway architecture:** A single gateway process routes conversations from all supported messaging platforms (Telegram, Discord, Slack, WhatsApp, Signal) and the terminal UI to the same agent instance, preserving conversation continuity across platforms.

## Key Features [coverage: high — 1 source]

- **40+ tools** with a configurable toolset system.
- **MCP integration:** Connect any MCP server for extended capabilities (documented in full).
- **Six terminal backends:** local, Docker, SSH, Singularity, Modal, and Daytona. Modal and Daytona support serverless persistence — the environment hibernates when idle and wakes on demand.
- **Full TUI:** Multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, streaming tool output.
- **Multi-platform messaging gateway:** Telegram, Discord, Slack, WhatsApp, Signal, and Email — all from a single gateway process. Includes voice memo transcription and cross-platform conversation continuity.
- **Model agnosticism:** Switch providers with `hermes model`. Supported out of the box: Nous Portal (300+ models), OpenRouter (200+ models), NovitaAI, NVIDIA NIM (Nemotron), Xiaomi MiMo, z.ai/GLM, Kimi/Moonshot, MiniMax, Hugging Face, OpenAI, or any custom endpoint.
- **Nous Portal integration:** One-command setup (`hermes setup --portal`) provides unified access to web search (Firecrawl), image generation (FAL), TTS (OpenAI), and a cloud browser (Browser Use) under a single subscription — no separate API keys.
- **Research tooling:** Batch trajectory generation and trajectory compression for training tool-calling models.
- **Context files:** Project context files that shape every conversation.
- **Security:** Command approval gates, DM pairing, container isolation.
- **OpenClaw migration:** Automatic import of settings, memories, skills, API keys, and workspace instructions from an existing OpenClaw install.
- **Cross-platform install:** Linux, macOS, WSL2, Termux, native Windows (PowerShell one-liner with bundled MinGit, no admin required), and Android/Termux with curated extras.

## Tech Stack [coverage: high — 1 source]

- **Primary language:** Python (Python 3.11)
- **Package manager:** uv
- **Deployment model:** Self-hosted; supports local process, Docker, SSH remote, Singularity (HPC), Modal (serverless), and Daytona (cloud dev environments). A gateway process handles messaging platform bridges.
- **Runtime dependencies:** Node.js (bundled on Windows), ripgrep, ffmpeg (for voice), portable MinGit on Windows.
- **Memory backend:** FTS5 (SQLite full-text search) for session search.
- **User modeling:** Honcho (plastic-labs/honcho) for dialectic user profiling.
- **Skills standard:** agentskills.io open standard for cross-agent skill sharing.
- **License:** MIT.

## Traction [coverage: high — 1 source]

- **194,575 stars** on GitHub — exceptionally high for a repo created in July 2025, indicating rapid viral growth within approximately one year of launch.
- Active development: last pushed 2026-06-16, less than two weeks before the scrape date.
- Community presence: Discord (discord.gg/NousResearch), a public Skills Hub at agentskills.io, and documented migration from a predecessor project (OpenClaw).
- Active third-party integrations: computer-use-linux MCP server (avifenesh/computer-use-linux) and HermesClaw community WeChat bridge (AaronWong1999/hermesclaw).
- README localized to Chinese and Urdu, indicating broad international adoption.

## Use Cases [coverage: medium — 1 source]

- **Personal AI assistant with long-term continuity:** Persistent memory and user modeling make it well-suited for ongoing personal productivity use where context accumulation over weeks/months matters.
- **Automation and scheduled tasks:** Built-in cron scheduler with messaging-platform delivery supports unattended daily reports, nightly backups, and weekly audits authored in natural language.
- **Multi-platform reachability:** Users who want to interact with the same agent from a terminal, Telegram, Discord, and WhatsApp without losing conversation state.
- **Self-hosted, cloud-agnostic deployment:** Teams or individuals who need full infrastructure control and cannot use hosted agent services — runs on anything from a $5 VPS to a GPU cluster.
- **AI/ML research:** Batch trajectory generation and trajectory compression pipelines for training or fine-tuning tool-calling models.
- **Developer productivity:** Code-focused workflows via the terminal backend, MCP server ecosystem, subagent delegation, and RPC-based Python scripting.
- **Emerging-market and mobile use:** Termux/Android support and WeChat bridge coverage extend reach beyond desktop-first tooling.

## Related Frameworks [coverage: medium — 1 source]

- **OpenClaw / ClawdBot / OpenClaw variants:** Hermes provides a first-class migration path from OpenClaw (`hermes claw migrate`), suggesting OpenClaw is a direct predecessor or close competitor in the same niche. Topics reference `openclaw`, `clawdbot`, and `moltbot`, implying these are related or prior projects in the same lineage.
- **Claude Code:** Explicitly referenced in topics and in the known Hermes bug report (NousResearch/hermes-agent#23450 re: `include: ["reasoning.encrypted_content"]`). Hermes and Claude Code occupy adjacent space (terminal AI agents) but differ substantially: Claude Code is editor- and codebase-focused, while Hermes is a general-purpose persistent agent with a learning loop, messaging gateway, and multi-backend deployment.
- **OpenAI Codex / ChatGPT-based agents:** Topics list `codex` and `chatgpt`, positioning Hermes as model-agnostic and competitive with provider-locked assistants.
- **Standard agentic frameworks (LangGraph, CrewAI, AutoGen):** Hermes differs from graph-based or multi-agent orchestration frameworks by centering a single persistent agent with a self-improving skills layer, rather than composing fixed agent networks or workflow DAGs.
- **agentskills.io ecosystem:** Hermes participates in a shared open standard for agent skills, meaning skills are theoretically portable to other compatible agents in that ecosystem.

## Sources [coverage: high — 1 source]

- [[../../sources/github-NousResearch_hermes-agent]]
