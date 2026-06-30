---
topic: nanobot
last_compiled: 2026-06-29
source_count: 1
status: active
---

# nanobot

## Summary [coverage: high — 1 sources]

nanobot (HKUDS/nanobot) is an open-source, ultra-lightweight personal AI agent written in Python. Its value proposition is minimal core size paired with a practical full-feature surface: persistent goals, memory, multi-channel chat delivery, tool-calling, MCP integration, image generation, and a bundled WebUI — all self-hostable and inspectable. The design philosophy is "own your stack": a small, readable agent loop that users can customize and extend without being locked into a vendor platform.

Source scraped at: 2026-06-16T03:25:14Z. The project was created on 2026-02-02 and has been releasing updates daily or near-daily since launch, with the most recent push on 2026-06-16.

## Core Pattern [coverage: high — 1 sources]

nanobot centers on a single agent loop: incoming messages from any connected channel are routed to the LLM, which decides when to invoke tools. Memory and skills are pulled in as context on demand rather than becoming a fixed orchestration layer. This keeps the hot path small and readable while still allowing arbitrarily many channels, tools, and memory backends to be attached.

Key abstractions:

- **Agent loop** — the LLM drives all tool decisions; no hardcoded workflow graphs
- **`/goal`** — a persistent sustained-objective command introduced in v0.2.0 that holds a long-horizon mission across turns and across sessions
- **Dream memory** — a two-stage memory system (introduced in v0.1.5) that stores and retrieves context; line-age tracking was added later for finer recall
- **Skills** — composable, discoverable capability units; the ClawHub registry allows installing public community skills
- **Model presets + fallback models** — named presets enable `/model` hot-switching and automatic fallback to backup models when a primary provider fails
- **AutoCompact** — automatic context-window compaction for long-running sessions

## Key Features [coverage: high — 1 sources]

- **MCP support** — Model Context Protocol integration added in v0.1.4 (2026-02-14); supports multiple MCP servers, custom auth headers, SSE transport, MCP resources and prompts exposed as tools, and MCP presets
- **WebUI** — bundled inside the published wheel (no separate build step); served over WebSocket on port 8765; features thought/response timelines, live file-edit activity, project workspaces, model controls, locale switcher, and LAN access
- **Multi-channel delivery** — Telegram, Discord, Slack, Feishu/Lark, WeChat, WeCom, QQ, Teams, Matrix, WhatsApp, Signal, DingTalk, Email, and a WebSocket channel; each channel supports threading, media, and platform-native formatting
- **Multi-provider model routing** — native SDKs for OpenAI, Anthropic, AWS Bedrock, Azure OpenAI, VolcEngine, StepFun, Skywork, MiniMax, Moonshot/Kimi, DeepSeek, Qwen, Mistral, Novita, Xiaomi MiMo, LM Studio, vLLM, Ollama, NVIDIA NIM, Hugging Face, and OpenRouter; OpenAI-compatible endpoint for third-party integrations
- **Image generation** — end-to-end pipeline added in v0.2.0; supports Zhipu, MiniMax, Gemini, and other image providers via a registry
- **Web search** — multi-provider (Kagi, Olostep, configurable BYO keys); web proxy support
- **Cron / scheduling** — natural-language cron reminders with durable persistence; macOS LaunchAgent and Linux service deployment
- **OpenAI-compatible API** — SSE streaming; lets other tools connect to nanobot as if it were an OpenAI endpoint
- **Python SDK** — composable agent lifecycle hooks for programmatic integration
- **Langfuse / LangSmith observability** — optional tracing integrations
- **Document extraction** — Office document reading; configurable extraction controls
- **Security** — shell allow-list, workspace path guards, configurable access controls, session poisoning fix
- **Interactive setup wizard** — `nanobot onboard --wizard` with provider autocomplete

## Tech Stack [coverage: high — 1 sources]

- **Primary language:** Python (requires Python 3.11+; CI covers Python 3.14 and Windows)
- **Install:** PyPI (`nanobot-ai`), `uv tool install`, or source; one-command shell installer for macOS/Linux and PowerShell installer for Windows
- **LLM SDKs:** native `openai` and `anthropic` Python SDKs (litellm dependency was removed in v0.1.4.post6 in favor of direct SDKs)
- **WebUI:** Vite-based frontend bundled into the wheel; served over WebSocket
- **Deployment:** Docker, Linux systemd service, macOS LaunchAgent, or bare process
- **Config:** JSON (`~/.nanobot/config.json`)
- **Notable dependencies:** Jinja2 (response templates), Whisper (voice transcription)
- **License:** MIT

## Traction [coverage: high — 1 sources]

- **44,235 GitHub stars** as of scrape date — exceptionally high for a project that launched on 2026-02-02 (approximately four and a half months old at scrape time)
- **Daily release cadence** maintained consistently from launch through June 2026; versioned minor releases roughly every 1–2 weeks (v0.1.3.post4 through v0.2.1 in the scraped history)
- **Community:** Discord server, Feishu group, WeChat group; Twitter/X account (`@nanobot_project`)
- **Documentation site:** nanobot.wiki with multilingual support (English, Simplified Chinese, Traditional Chinese, Spanish, French, Indonesian, Japanese, Korean, Russian, Vietnamese)
- **Open source partners listed:** Kimi (Moonshot) and MiniMax
- **Contributor graph** active; contributions tracked via contrib.rocks
- **PyPI package** (`nanobot-ai`) with download badge visible in README, indicating meaningful PyPI adoption

## Use Cases [coverage: medium — 1 sources]

nanobot is explicitly positioned for personal and team daily-driver use rather than enterprise workflow orchestration:

- **Personal AI assistant** — persistent memory + goals across a preferred chat app (Telegram, WeChat, Slack, etc.) rather than a standalone chat interface
- **24/7 market or news monitoring** — real-time web search with scheduled reminders and summarization
- **Coding assistant** — full-stack software engineering tasks via CLI or chat; integrates with Codex provider
- **Daily routine management** — schedule automation, cron reminders, calendar integration (on roadmap)
- **Personal knowledge base** — memory-backed recall for long-horizon research and note-taking
- **Self-hosted LLM experimentation** — Ollama, vLLM, and LM Studio support for running fully local stacks
- **Automation gateway** — OpenAI-compatible API and Python SDK enable connecting nanobot as a backend for other tools or pipelines

## Related Frameworks [coverage: medium — 1 sources]

- **Open Interpreter** — similar personal coding-agent positioning; nanobot is more channel/chat-native and adds persistent goals and MCP out of the box
- **Claude Code / Codex CLI** — nanobot's topics list (`claude-code`, `codex-cli`) signals intentional positioning alongside these tools; nanobot wraps or routes to Codex and Claude Code providers rather than replacing them
- **AutoGen / CrewAI / LangGraph** — multi-agent orchestration frameworks with heavier abstractions; nanobot deliberately avoids workflow graphs and keeps a single-agent loop with tool composition
- **OpenHands** — self-hosted coding agent; nanobot is broader (non-coding automation, chat channels) but lighter-weight
- **n8n / Zapier** — automation platforms; nanobot overlaps on scheduling and channel integrations but stays LLM-first rather than node-graph-first
- **Botpress / Rasa** — chat-bot platforms; nanobot differs by keeping the LLM in the decision loop rather than using intent classification

## Sources [coverage: high — 1 sources]

- [[../../sources/github-HKUDS_nanobot]]
