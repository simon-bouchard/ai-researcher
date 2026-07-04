---
topic: jackwener_opencli
last_compiled: 2026-07-03
sources:
  - ../../sources/github-jackwener_OpenCLI
status: active
---

# OpenCLI

## Summary [coverage: low — 1 source]

Scraped 2026-06-16T03:25:24Z. OpenCLI is a JavaScript tool that converts websites into deterministic CLI interfaces and enables AI agents to operate any website through the user's already logged-in Chrome browser. It provides three surfaces in one: built-in adapters for 100+ popular sites (Bilibili, Twitter, LinkedIn, Reddit, HackerNews, Zhihu, etc.), a `browser` primitive layer for ad-hoc AI agent-driven navigation/interaction, and an adapter authoring system so agents can write new site adapters end-to-end. With 24,476 stars, it was created in March 2026 and targets the intersection of browser automation and AI agent tooling.

## Core Pattern [coverage: low — 1 source]

- Browser Bridge: lightweight Chrome extension + local daemon connects to the user's live logged-in Chrome session (no headless browser, real cookies/auth)
- Adapter pattern: site-specific command adapters (SPA/SSR/JSONP/Token/Streaming) with declared auth strategies (PUBLIC/COOKIE/INTERCEPT/UI/LOCAL)
- Skill-based AI agent integration: install `opencli-browser`, `opencli-adapter-author`, and other skills into Claude Code, Cursor, etc. — the agent drives `opencli browser` commands internally
- Session management: named sessions, tab leases, persistent or ephemeral site sessions, CDP endpoint support for Electron apps
- Plugin system: install third-party adapters from GitHub repos; community adapter registry
- CLI Hub: unified passthrough for local CLI tools (gh, docker, vercel, discord-cli, notion, etc.) and desktop Electron app adapters

## Key Features [coverage: low — 1 source]

- 100+ built-in site adapters with structured output (table/json/yaml/md/csv)
- AI agent skills: `opencli-browser` (ad-hoc browser driving), `opencli-adapter-author` (write new adapters), `opencli-autofix` (repair broken adapters), `opencli-browser-sitemap`, `opencli-sitemap-author`, `opencli-usage`
- DOM snapshot-based interaction (not screenshots) for structured page reading
- Full browser command set: navigate, click, type, fill, select, keys, wait, get, find, extract, screenshot, scroll, network interception, tab management
- Download support: images/videos from xiaohongshu, bilibili, twitter, zhihu, weixin, pixiv, 1688, xiaoyuzhou (audio+transcript)
- Desktop Electron app adapters: Cursor, ChatGPT App, Codex, Trae, Discord via CDP
- Unix exit codes for CI/script branching (`sysexits.h` conventions)
- Multi-Chrome-profile support with named aliases

## Tech Stack [coverage: low — 1 source]

- Language: JavaScript
- Runtime: Node.js >= 20
- Package: `@jackwener/opencli` on npm
- Browser integration: Chrome extension (Chrome Web Store) + local daemon on port 19825
- CDP (Chrome DevTools Protocol) for remote browser and Electron app control
- Skills format: compatible with Claude Code, Cursor, and other skill-aware agents

## Traction [coverage: low — 1 source]

- 24,476 stars
- Created 2026-03-14; pushed 2026-06-15 — approximately 3 months old at scrape time
- Community plugins already published (GitHub Trending, hot-digest, Juejin, VK)
- Chinese and English documentation; strong presence in Chinese developer community (Bilibili, Zhihu, Xiaohongshu adapters prominent)

## Use Cases [coverage: low — 1 source]

- AI agents that need to interact with websites using the user's existing authenticated sessions (avoiding API key setup or scraping blocks)
- Scraping/extracting data from sites with no public API (social platforms, internal tools)
- Automating repetitive browser workflows by describing them in natural language to an AI agent
- Writing reusable adapters for sites and sharing them as plugins
- Desktop Electron app automation via CDP (Cursor, ChatGPT App, Codex)
- Wrapping existing CLI tools under a unified `opencli <tool>` discovery surface

## Related Frameworks [coverage: low — 1 source]

- [[browser-use_browser-harness]] — browser automation framework; OpenCLI is more opinionated with its adapter/skill layer and focuses on logged-in browser sessions
- [[gitlawb_openclaude]] — coding agent CLI that can install OpenCLI skills; complementary rather than competing
- [[gptme_gptme]] — terminal agent with built-in Playwright browser tool; OpenCLI's `opencli-browser` skill can extend agents like gptme
- [[nousresearch_hermes-agent]] — agent CLI that can use OpenCLI as a browser automation backend via skill installation
- [[e2b-dev_e2b]] — remote sandboxed execution environment; OpenCLI uses the user's local Chrome session instead of a cloud sandbox

## Sources

- [[../../sources/github-jackwener_OpenCLI]]
