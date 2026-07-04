---
topic: gptme_gptme
last_compiled: 2026-07-03
sources:
  - ../../sources/github-gptme_gptme
status: active
---

# gptme

## Summary [coverage: low — 1 source]

Scraped 2026-06-16T03:10:39Z. gptme is a personal AI agent that runs anywhere a terminal runs — laptops, SSH sessions, tmux, headless servers, CI pipelines — and is one of the first agent CLIs, dating from Spring 2023. It is provider-agnostic (Anthropic, OpenAI, Google, xAI, DeepSeek, OpenRouter, llama.cpp) and ships with a rich built-in toolset covering shell execution, Python, file patching, web browsing via Playwright, vision, RAG, GitHub CLI, tmux, desktop computer-use, and sub-agents. Beyond interactive use, gptme is designed to run as a persistent autonomous agent via the gptme-agent-template scaffold, with a reference production agent ("Bob") running continuously since late 2024.

## Core Pattern [coverage: low — 1 source]

- Interactive terminal chat loop with self-correcting output feedback
- Persistent autonomous agent mode: git-tracked workspace ("brain"), scheduled or event-driven run loops (systemd/launchd), task queue, meta-learning lessons system
- Sub-agents: spawn parallel or isolated sub-agents via the `subagent` tool
- Multi-agent coordination: file leases, message bus, work claiming for concurrent agents
- Plugin system: Python-package plugins with tools, hooks, commands; skills (Anthropic format); lessons (contextual guidance auto-injected by keyword/tool/pattern matching); hooks (lifecycle events)
- Model routing: pick fast/cheap models for triage, powerful models for coding, per-task
- Guardrails: input selectors, pre-action lessons injection, post-action hooks and pre-commit checks

## Key Features [coverage: low — 1 source]

- Rich built-in tools: shell, ipython, read, save/append, patch/morph, browser (Playwright), vision, screenshot, RAG, gh (GitHub CLI), tmux, computer (full desktop), subagent, chats
- MCP (Model Context Protocol): discovery and dynamic loading of MCP servers
- ACP (Agent Client Protocol): drop-in coding agent in Zed and JetBrains IDEs
- Web UI at chat.gptme.org (self-hostable); REST API server
- Lessons system: contextual guidance auto-included based on keywords, tools, patterns
- Code intelligence via gptme-codegraph: tree-sitter call graphs, symbol extraction, 9 MCP tools
- Background jobs, form tool, cost tracking, content-addressable storage
- JSONL output mode (`--output-format json`) for CI/automation
- Non-interactive mode (`-n`) for scripting with no user interaction possible

## Tech Stack [coverage: low — 1 source]

- Language: Python 3.10+
- Package: `gptme` on PyPI; extras for browser (`[browser]`), all features (`[all]`)
- Installation: pipx, uv, or pip
- Local models: llama.cpp via OpenAI-compatible server
- Config: `~/.config/gptme/config.toml`
- Community plugins in `gptme-contrib` repo
- Ecosystem: gptme-webui (React), gptme-rag, gptme.vim, gptme-tauri (WIP desktop), gptme.ai (WIP cloud)

## Traction [coverage: low — 1 source]

- 4,332 stars
- Created 2023-03-24; pushed 2026-06-16 — over 3 years of active development
- One of the first agent CLIs publicly released (Spring 2023); Show HN 2024
- Discord community; X/Twitter @gptmeorg
- Reference autonomous agent "Bob" contributing to open source since late 2024
- Regular versioned releases (v0.31.0 at scrape time)

## Use Cases [coverage: low — 1 source]

- Coding assistance and autonomous code generation, testing, CI fix loops in the terminal
- Persistent autonomous agents that run on a schedule, monitor GitHub, post on social media
- Multi-agent setups with specialized concurrent agents sharing a workspace
- Research automation: web browsing, data collection, literature review
- Local-first or fully offline agent operation via llama.cpp
- IDE integration as a coding agent (Zed, JetBrains) via ACP

## Related Frameworks [coverage: low — 1 source]

- [[gitlawb_openclaude]] — also a terminal coding-agent CLI; OpenClaude is newer and multi-provider-focused, gptme has a deeper autonomous-agent ecosystem
- [[nousresearch_hermes-agent]] — another terminal agent CLI; gptme distinguishes itself with the persistent autonomous agent template and lessons system
- [[jackwener_opencli]] — browser-to-CLI bridge that can be installed as a skill in gptme-style agents
- [[langroid_langroid]] — Python multi-agent framework; langroid targets developer library use, gptme targets end-user terminal operation
- [[letta-ai_letta]] — persistent memory-centric agent platform; gptme achieves persistence via git-tracked workspace rather than a managed memory service

## Sources

- [[../../sources/github-gptme_gptme]]
