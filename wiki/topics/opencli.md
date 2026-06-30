---
topic: OpenCLI
last_compiled: 2026-06-29
source_count: 1
status: active
---

# OpenCLI

## Summary [coverage: high — 1 source]

OpenCLI is a JavaScript CLI tool that converts any website into a deterministic command-line interface and exposes a browser automation layer for AI agents to operate through the user's own logged-in Chrome session. Its core value proposition is dual: it gives humans reliable, scriptable commands for over 100 web platforms without writing code, and it gives AI agents (Claude Code, Cursor, etc.) structured access to any website by operating the user's real browser — bypassing authentication, paywalls, and session state that headless scrapers cannot reach. The project was created on 2026-03-14 and was last updated 2026-06-15. Source scraped 2026-06-16.

---

## Core Pattern [coverage: high — 1 source]

OpenCLI combines two distinct automation patterns in one tool:

**Adapter pattern (human-facing):** Pre-built adapters encode site-specific API or DOM interaction logic as named subcommands (`opencli bilibili hot`, `opencli twitter timeline`). Each adapter is a standalone module that can be authored, ejected, modified, and reinstalled independently. Adapters target one of five auth patterns (PUBLIC, COOKIE, INTERCEPT, UI, LOCAL) and one of four site patterns (SPA, SSR, JSONP, Token/Streaming).

**Browser-primitive pattern (agent-facing):** The `opencli browser <session>` command set exposes a low-level Chrome DevTools Protocol (CDP) bridge as named subcommands (`open`, `click`, `fill`, `extract`, `network`, `eval`, `screenshot`, etc.). AI agents receive these as a skill (`opencli-browser`) and can drive any page through the user's real Chrome profile. The agent reads structured DOM snapshots — not screenshots — which keeps context size low and parsing deterministic.

The two patterns are composable: new adapters are authored by calling browser primitives during a recon session, then encoding the discovered flow into a reusable module. A separate `opencli-adapter-author` skill guides agents through the full recon-to-verify loop.

There is no multi-agent orchestration layer built into OpenCLI itself. It is a tool layer consumed by external agents, not an agent runtime.

---

## Key Features [coverage: high — 1 source]

- **100+ built-in site adapters** covering Xiaohongshu, Bilibili, Zhihu, Twitter/X, Reddit, HackerNews, LinkedIn, Amazon, Upwork, Gemini, Claude, NotebookLM, Slock, GeoGebra, Douyin, Spotify, Weibo, Pixiv, Google Scholar, and many more.
- **AI agent skill system:** Six installable skills for Claude Code and Cursor — `opencli-browser` (ad-hoc browser driving), `opencli-adapter-author` (end-to-end adapter authoring), `opencli-autofix` (repair broken adapters), `opencli-browser-sitemap` (sitemap-aware navigation), `opencli-sitemap-author` (record stable site workflows), `opencli-usage` (reference). Installed via `npx skills add jackwener/opencli`.
- **CLI hub:** Unified passthrough for existing local binaries (gh, docker, vercel, wrangler, obsidian, lark-cli, Notion, DingTalk, WeChat Work, tg-cli, discord-cli, wx-cli). Register any binary with `opencli external register`.
- **Desktop app adapters via CDP:** Supports Electron apps — Cursor, Trae CN, Codex, Antigravity, ChatGPT App, ChatWise, Qoder, Discord, Doubao, Trae SOLO — without a Chrome extension, using `OPENCLI_CDP_ENDPOINT`.
- **Download support:** Images, video, audio, and article export (Markdown) across Xiaohongshu, Bilibili, Twitter, Zhihu, Weixin, Pixiv, Douban, 1688, Xiaoyuzhou podcast. Video download delegates to `yt-dlp`.
- **Multi-format output:** All built-in commands emit `table`, `json`, `yaml`, `md`, or `csv` via `--format` / `-f`, enabling direct pipe to `jq` or LLM prompts.
- **Multi-profile Chrome support:** Each Chrome profile runs its own Browser Bridge extension instance; profiles are listed and aliased with `opencli profile`.
- **Plugin system:** Community adapters distributed as npm-compatible packages, installed via `opencli plugin install github:user/repo`. Four community plugins available at time of scraping.
- **Unix exit codes:** Follows `sysexits.h` (0 success, 66 empty, 69 bridge down, 75 timeout, 77 auth required, 78 config error, 130 Ctrl-C) for CI/script compatibility.
- **Session management:** Browser sessions are explicit and named; tab leasing is controlled (`persistent` vs `ephemeral`); idle cleanup is automatic.

No MCP server interface is present. OpenCLI uses its own skills distribution format, not the Model Context Protocol.

---

## Tech Stack [coverage: high — 1 source]

- **Language:** JavaScript (Node.js >= 20 required)
- **Distribution:** npm package (`@jackwener/opencli`), global install
- **Browser integration:** Chrome/Chromium via a lightweight Browser Bridge Chrome extension (Chrome Web Store) plus a local daemon on port 19825. Communication over HTTP to the daemon, which relays to the extension.
- **Protocol:** Chrome DevTools Protocol (CDP) for both extension-backed and direct Electron app control
- **Browser automation library:** Playwright (listed in repo topics; underlying DOM snapshot and interaction primitives)
- **Skill distribution:** `npx skills add` (separate `skills` CLI package, not npm scripts)
- **Desktop adapters:** CDP endpoint targeting (`OPENCLI_CDP_ENDPOINT`, `OPENCLI_CDP_TARGET`)
- **Configuration:** Environment variables (`OPENCLI_DAEMON_PORT`, `OPENCLI_PROFILE`, `OPENCLI_WINDOW`, timeouts, verbose flags); no central config file mentioned beyond per-adapter site knowledge stored in `~/.opencli/`
- **License:** Apache-2.0

---

## Traction [coverage: high — 1 source]

- **24,476 GitHub stars** as of scrape date (2026-06-16) — exceptionally high for a tool created only three months prior (2026-03-14), indicating rapid viral growth.
- Last commit pushed 2026-06-15, one day before scraping — actively maintained.
- Community plugin ecosystem already present (4 published plugins covering GitHub Trending, multi-platform trending digest, Juejin, VK).
- Chinese-language documentation (`README.zh-CN.md`) and heavy coverage of Chinese platforms (Xiaohongshu, Bilibili, Zhihu, Douyin, Weibo, 1688, Xiaoyuzhou, Weixin, Lark, DingTalk, WeChat Work) suggests strong adoption in Chinese developer community.
- Chrome Web Store extension published under official listing.
- Topics: `ai-agent`, `ai-agents`, `ai-tools`, `browser-automation`, `browser-use`, `cli`, `playwright`.

---

## Use Cases [coverage: high — 1 source]

- **AI agent browser access:** Giving an agent (Claude Code, Cursor) the ability to operate any logged-in website on behalf of the user — fill forms, read notifications, post content, extract data — without re-authenticating or scraping behind a login wall.
- **Personal automation scripts:** Replacing one-off browser sessions with repeatable CLI commands for routine tasks (check Zhihu hot, download Bilibili video, post to Twitter, read LinkedIn inbox).
- **Data extraction pipelines:** Piping structured JSON/CSV output from 100+ platforms into downstream tools (`jq`, spreadsheets, LLM prompts).
- **Adapter authoring with AI assistance:** Using the `opencli-adapter-author` skill to teach an agent to discover, encode, and maintain site-specific automation — scaling adapter coverage without manual Playwright scripting.
- **CLI unification:** Wrapping all local binaries and platform CLIs under one discovery surface for both humans and agents.
- **Content downloading:** Archiving media and articles from Chinese and Western platforms for offline use.
- Less suited for: headless server-side scraping at scale (requires a running Chrome instance with the user's session), or use cases where the agent cannot run `opencli` locally.

---

## Related Frameworks [coverage: medium — 1 source]

- **Browser Use (python):** The `browser-use` topic tag is a direct reference. Browser Use is a Python library (and companion cloud service) that gives LLMs a browser via Playwright. OpenCLI overlaps in goal but differs in approach: Browser Use is a Python library consumed in agent code; OpenCLI is a CLI tool with a skills interface, uses the user's real logged-in Chrome profile (not a headless browser), and provides a pre-built adapter library for 100+ specific sites.
- **Playwright / Puppeteer:** OpenCLI sits above Playwright and abstracts its primitives into named CLI subcommands. Playwright itself requires code; OpenCLI makes those primitives available to an LLM agent as natural-language-directed commands.
- **AgentQL:** AgentQL provides semantic DOM querying for browser agents. OpenCLI uses structured DOM snapshots through CDP rather than semantic selectors; the two could be complementary.
- **Browserbase / Steel:** Cloud browser-as-a-service products that give agents a remote headless browser. OpenCLI explicitly contrasts by using the user's local, logged-in Chrome — no remote browser subscription needed, and session state is always fresh.
- **MultiOn:** A browser agent service for web automation. Like OpenCLI's agent mode, it operates real browsers; unlike OpenCLI, it is a hosted API service rather than a local CLI tool with a skills interface.
- **Hermes (NousResearch):** Used in this project as the orchestrating agent that calls OpenCLI-style tools. OpenCLI would be a natural tool layer for any Hermes-like agent runtime.

---

## Sources [coverage: high — 1 source]

- [[../../sources/github-jackwener_OpenCLI]]
