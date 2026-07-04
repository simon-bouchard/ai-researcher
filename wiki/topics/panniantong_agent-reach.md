---
topic: panniantong_agent-reach
last_compiled: 2026-07-03
sources:
  - ../../sources/github-Panniantong_Agent-Reach
status: active
---

# Agent Reach

## Summary [coverage: low — 1 source]

Scraped 2026-06-16T03:25:16Z. Agent Reach is a capability layer (not a framework) that gives AI agents access to internet content across multiple platforms — Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, RSS, and web pages — without requiring paid API keys. It handles tool selection, installation, health-checking, and backend routing, while the actual reads are performed directly by the upstream CLI tools the agent calls. With 30,528 stars created in February 2026, it grew rapidly by solving a concrete friction point: getting a coding agent to read social media and video content without per-platform configuration headaches.

## Core Pattern [coverage: low — 1 source]

- Capability layer pattern: Agent Reach selects, installs, and routes to upstream tools; agents call those tools directly with no wrapper layer
- Multi-backend routing per channel: each platform has an ordered list of backends (primary + fallbacks); first fully working backend wins
- Agent-driven install: paste a single URL to the agent and it runs the entire setup autonomously
- SKILL.md registration: after install, agents discover which tool to call for each content type without explicit user instruction
- `agent-reach doctor` performs live backend probing (not just existence checks) and prescribes fixes for each broken channel

## Key Features [coverage: low — 1 source]

- Zero-cost internet access: all backends are open-source tools with no paid API keys required (optional ~$1/month proxy for server deployments)
- Platforms supported out-of-the-box: web pages (Jina Reader), YouTube subtitles (yt-dlp), RSS (feedparser), GitHub (gh CLI), Bilibili search (bili-cli), Exa semantic search (via MCP/mcporter)
- Platforms requiring login-state configuration: Twitter/X, Reddit, XiaoHongShu, LinkedIn
- Self-healing routing: when a backend is blocked or deprecated, the channel file switches to the next candidate (e.g., yt-dlp replaced by bili-cli for Bilibili after B站 blocked yt-dlp in June 2026)
- Safe/dry-run install modes; uninstall clears all credentials and skill files
- Cookie-based auth for login-required platforms; credentials stored locally at `~/.agent-reach/config.yaml` with 600 permissions

## Tech Stack [coverage: low — 1 source]

- Primary language: Python 3.10+
- MCP integration: Exa search via mcporter (Model Context Protocol)
- Key upstream tools: yt-dlp, feedparser, gh CLI, bili-cli, twitter-cli, rdt-cli, OpenCLI, xiaohongshu-mcp, Jina Reader, linkedin-scraper-mcp
- Installation: `pip install agent-reach` + `agent-reach install`
- Compatible agents: Claude Code, Cursor, OpenClaw, Windsurf, Codex, and any agent that can run shell commands

## Traction [coverage: low — 1 source]

- 30,528 stars; created 2026-02-24, which implies extremely rapid growth (~4 months to 30k stars)
- Last pushed: 2026-06-12; active maintenance with same-month backend switches in response to platform changes
- Mirrored on AtomGit for mainland China access with auto-sync
- Community WeChat group; Twitter/X presence at @Neo_Reidlab

## Use Cases [coverage: low — 1 source]

- Giving a coding agent the ability to research across social media, video, and web without manual tool setup
- Competitive intelligence gathering: reading Twitter, Reddit, and YouTube content on a topic
- Chinese-market content access: Bilibili, XiaoHongShu, Xuejiu (stock info), Xiaoyuzhou podcast
- RSS-based monitoring and aggregation tasks
- Serverless agents on cloud VMs that need stable, free internet-access primitives

## Related Frameworks [coverage: low — 1 source]

- [[jackwener_opencli]] — OpenCLI is Agent Reach's preferred backend for Reddit and XiaoHongShu; Agent Reach acts as the routing layer on top of it
- [[nousresearch_hermes-agent]] — Hermes is an agent runtime; Agent Reach is a capability layer that could extend any agent's internet reach, including Hermes-based ones
- [[browser-use_browser-harness]] — Browser Harness handles login flows and web automation; Agent Reach explicitly positions it as the complement for high-friction scenarios (login, form submission, multi-step browser workflows)
- [[google_adk-python]] — ADK provides agent orchestration; Agent Reach provides the internet-content primitives those agents would consume
- [[ruvnet_ruflo]] — Ruflo is a meta-harness that adds memory and swarm coordination; Agent Reach fills a complementary gap (internet content access) that Ruflo does not directly address

## Sources

- [[../../sources/github-Panniantong_Agent-Reach]]
