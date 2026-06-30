---
topic: gptme
last_compiled: 2026-06-29
source_count: 1
status: active
---

# gptme

## Summary [coverage: high — 1 source]

gptme is a personal AI agent that runs anywhere a terminal runs — laptops, SSH sessions, tmux, headless servers, and CI pipelines. Its core value proposition is being provider-agnostic, local-first, and unconstrained: it ships with a rich built-in toolset (shell execution, Python, web browsing via Playwright, vision, file patching, RAG, and more) without requiring any external service beyond an LLM provider. It is a capable coding agent but general-purpose enough for knowledge-work broadly. It positions itself as an alternative to Claude Code, Codex, Cursor, and Warp, and claims to be one of the first agent CLIs (Spring 2023), still in very active development.

Source data scraped 2026-06-16 (pushed_at: 2026-06-16). The project has 4,332 GitHub stars and was created 2023-03-24.

## Core Pattern [coverage: high — 1 source]

gptme follows a **tool-calling loop** pattern: the LLM issues tool calls, tool output is fed back into the conversation as observations, and the agent self-corrects until the task is done. The pattern is interactive by default but supports fully autonomous non-interactive mode (`--non-interactive`, `-n`) for scripting and CI. Key abstractions:

- **Tools** — the primary extension point; each tool is a first-class capability (shell, ipython, browser, patch, morph, rag, subagent, etc.) callable by the LLM.
- **Subagent tool** — spawns child agents for parallel or isolated subtasks, enabling lightweight multi-agent decomposition from within a single session.
- **Lessons system** — contextual guidance documents auto-injected into the conversation based on keyword, tool, and pattern matching. Distinguishes between interactive and autonomous modes. Captures team best-practices or domain knowledge that steers agent behavior pre-action.
- **Plugins / Hooks / Skills** — layered extensibility: plugins are Python packages; hooks run custom code at lifecycle events (before/after tool calls, conversation start); skills are lightweight workflow bundles (Anthropic format) that auto-load by name.
- **Persistent autonomous agent mode** — via `gptme-agent-template`: git-tracked workspace ("brain") with journal, task queue, knowledge base, and lessons. Agents run on schedules (systemd/launchd) or event-driven loops, with multi-agent coordination via file leases and a message bus.

The guardrail stack layers input selectors (focusing work), pre-action lessons (steering behavior), and output hooks plus pre-commit checks (verifying results).

## Key Features [coverage: high — 1 source]

- **MCP support** — built-in; auto-discovers and dynamically loads MCP servers as native tools. Supported out-of-the-box with `pipx install gptme`. Includes gptme-codegraph (9 MCP tools for tree-sitter call graphs, symbol extraction, blast/impact analysis).
- **ACP (Agent Client Protocol)** — makes gptme a drop-in coding agent for Zed and JetBrains IDEs; editor sends requests, gptme executes with its full toolset.
- **RAG tool** — retrieval over local files (semantic search); also available as a standalone `gptme-rag` package.
- **Web browsing** — Playwright-based browser tool; can navigate, search, and extract from live web pages.
- **Vision** — processes images referenced in prompts, desktop screenshots, and web page screenshots.
- **Computer use** — full desktop GUI interaction via the `computer` tool.
- **Web UI and REST API** — modern React interface at chat.gptme.org (self-hostable via `gptme-server` + `gptme-webui`); simple built-in web UI bundled in the Python package.
- **Model routing** — pick different models per task (fast/cheap for triage, powerful for coding); supports 100+ models via OpenRouter or fully local via llama.cpp.
- **Background jobs and cost tracking** — added in v0.31.0 (2025-12).
- **Content-addressable storage** — added in v0.31.0.
- **Context compression** — added in v0.30.0.
- **Auto-commit** — added in v0.28.0.
- **Pre-commit integration** — added in v0.27.0.
- **Local TTS** — Kokoro TTS support added in v0.27.0.
- **Fully local operation** — llama.cpp backend; no API key required.
- **GitHub Bot** — runs entirely in GitHub Actions; responds to issue/PR comments by making code changes autonomously.
- **Evaluation suite** — benchmark suite for testing model capabilities across tasks.
- **JSONL machine-readable output** — `--output-format json` for scripting/CI integration.

## Tech Stack [coverage: high — 1 source]

- **Primary language:** Python (3.10+ required)
- **Installation:** `pipx install gptme` or `uv tool install gptme`; extras include `[browser]` (Playwright) and `[all]`
- **LLM providers:** Anthropic (Claude), OpenAI (GPT), Google (Gemini), xAI (Grok), DeepSeek, OpenRouter (100+ models), llama.cpp (local, no key)
- **Web browsing:** Playwright
- **Code intelligence:** Tree-sitter (via gptme-codegraph)
- **Web UI:** React (gptme-webui)
- **Desktop app (WIP):** Tauri (gptme-tauri)
- **Deployment model:** Local-first CLI; optional self-hosted server (`gptme-server`); managed cloud service gptme.ai in progress
- **Config format:** TOML (`~/.config/gptme/config.toml`), YAML for agent workspaces
- **Code quality:** mypy, ruff, pyupgrade; high test coverage via Codecov
- **Community contrib packages:** gptme-codegraph (tree-sitter), gptme-consortium (multi-model consensus), gptme-imagen (image generation), gptme-lsp (LSP integration), gptme-ace (context optimization), gptme-gupp (work state persistence)

## Traction [coverage: high — 1 source]

- **4,332 GitHub stars** (as of 2026-06-16 scrape)
- **Launched Spring 2023** — one of the first agent CLIs; initial public release on Hacker News (2023-09-08, #37394845) and Reddit r/LocalLLaMA; second HN Show HN in 2024-08 (#41204256)
- **Viral attention:** First viral tweet Oct 2024 (Rohan Paul, @rohanpaul_ai), bringing widespread attention
- **Active release cadence:** v0.27 through v0.31 shipped between March 2025 and December 2025; last push 2026-06-16
- **PyPI presence** with tracked all-time downloads (pepy.tech) and daily download stats (pypistats)
- **Discord community** (discord.gg/NMaCmmkxWv) and GitHub Discussions active
- **Twitter/X account** @gptmeorg with follower count tracked
- **Production autonomous agent ("Bob")** has been running continuously since late 2024 — opens PRs, fixes CI, manages task queue, posts on Twitter, responds on Discord, writes blog posts — serving as a live proof-of-concept for the platform
- **gptme-contrib** community plugin repo created Jan 2025 with Twitter/X, Discord bot, email tools, and multi-agent plugins

## Use Cases [coverage: high — 1 source]

- **Coding and development** — write, refactor, debug, test code; self-corrects from test output; pre-commit integration validates changes; GitHub bot for PR-driven code changes
- **Shell expertise** — natural language to shell commands; no flag memorization; runs and verifies in real terminal
- **Persistent autonomous agents** — long-running agents (days/weeks) with their own workspace, task queue, and meta-learning via lessons; reference: Bob (GitHub: TimeToBuildBob)
- **Data analysis** — process and analyze data directly in terminal via IPython tool
- **Research automation** — web browsing + RAG + shell for literature review, data collection, analysis pipelines
- **Interactive learning** — experiment with new technologies hands-on in a guided loop
- **CI/CD pipelines** — non-interactive mode with JSONL output; headless server execution; GitHub Actions integration
- **DevOps** — server management, deployment automation via shell access
- **Multi-agent systems** — parallel specialized agents (e.g. Bob for engineering + Alice for personal assistant/orchestration) coordinating via shared file-based infrastructure

## Related Frameworks [coverage: medium — 1 source]

gptme self-positions against these tools (from its own comparison table):

- **Claude Code** — Anthropic's official terminal agent; similar terminal orientation and MCP support, but API-only (no local model support), no multi-agent, no plugin system, no web browsing. gptme predates it and supports 100+ models.
- **Cursor** — IDE-based coding assistant with extension support; no MCP, no web browsing, no autonomous agent mode, API-only. Different form factor (editor vs. terminal).
- **Warp** — terminal AI assistant (OpenAI-backed); no MCP, no plugin system, no web browsing, no multi-agent, no local models.
- **Codex (OpenAI)** — mentioned as alternative but no detailed comparison provided.
- **aider** — not compared directly but occupies similar "terminal coding agent" space; gptme is broader in scope (autonomous agents, web browsing, general knowledge-work).
- **Open Interpreter** — similar terminal-based code-executing agent; gptme differentiates on persistent autonomous agent infrastructure, lessons system, and ecosystem breadth.

## Sources [coverage: high — 1 source]

- [[../../sources/github-gptme_gptme]]
