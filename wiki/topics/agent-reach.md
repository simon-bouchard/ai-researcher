---
topic: agent-reach
last_compiled: 2026-06-29
source_count: 1
status: active
---

# Agent-Reach

## Summary [coverage: high — 1 source]

Agent-Reach is a Python CLI tool that gives AI agents structured access to a broad range of internet platforms — Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu (Little Red Book), LinkedIn, V2EX, RSS feeds, and the open web — without API fees. Rather than being an agent framework itself, it is a **capability layer**: it selects, installs, health-checks, and routes between the best available backend for each platform, and registers a `SKILL.md` file into the agent's skills directory so the agent autonomously knows which upstream tool to invoke for each task.

The project was created on 2026-02-24 and reached 30,528 stars by scrape date (2026-06-16T03:25:16Z), roughly four months after creation — an unusually rapid growth curve driven largely by Chinese-language social media and a mirror on AtomGit for mainland China access.

## Core Pattern [coverage: high — 1 source]

Agent-Reach does not wrap or orchestrate tools — it sits one layer above them, responsible for **selection, installation, diagnostics, and routing**. The core abstraction is a per-platform channel file (`channels/twitter.py`, `channels/bilibili.py`, etc.), each of which defines an ordered list of candidate backends. At runtime, the channel probes each backend in sequence, picks the first fully operational one, and records the decision. If a backend breaks (e.g., yt-dlp blocked by Bilibili anti-scraping in June 2026 → switched to bili-cli), the list is reordered without any code rewrite.

The agent never calls Agent-Reach at query time. Instead, after installation, the agent reads `SKILL.md` (registered into the agent's skills directory) and invokes upstream CLI tools directly — `twitter search "..."`, `yt-dlp --write-sub`, `gh repo view`, `bili search`, etc. Agent-Reach itself is only re-invoked for diagnostics (`agent-reach doctor`) or updates.

Installation is bootstrapped by pasting a single URL into any CLI-capable agent; the agent fetches and executes the install manifest autonomously with no human step-through required.

## Key Features [coverage: high — 1 source]

- **Zero-API-fee internet access** across 12+ platforms: web pages (Jina Reader), YouTube (yt-dlp), RSS (feedparser), GitHub (gh CLI), Twitter/X (twitter-cli → OpenCLI → bird), Reddit (OpenCLI → rdt-cli), Bilibili (bili-cli → OpenCLI → search API), XiaoHongShu (OpenCLI → xiaohongshu-mcp → xhs-cli), LinkedIn (linkedin-scraper-mcp → Jina Reader), V2EX, Xueqiu (Chinese stocks), Xiaoyuzhou podcast (Whisper transcription).
- **MCP integration**: Exa semantic search is exposed via [mcporter](https://github.com/nicobailon/mcporter) as an MCP server, providing free web-wide semantic search without an API key.
- **`agent-reach doctor`**: probes every channel's current backend in real-time, reports which is active, and provides fix prescriptions for broken backends.
- **SKILL.md auto-registration**: installs a skills guide into the agent's skills directory so agents understand which tool to call for "search Twitter," "watch YouTube," "scrape Reddit," etc., without explicit user instruction on each query.
- **Safe / dry-run modes**: `--safe` lists required changes without executing; `--dry-run` previews all operations without side effects.
- **Pluggable channels**: each platform is one independent file — replacing a backend or adding a new channel requires no changes to other components.
- **Self-updating**: update is bootstrapped the same way as install (one URL to the agent).
- **Credential security**: tokens and cookies stored locally in `~/.agent-reach/config.yaml` with `600` permissions; never uploaded.

## Tech Stack [coverage: high — 1 source]

- **Primary language**: Python 3.10+
- **Distribution**: pip / pipx (`pip install agent-reach`)
- **Key bundled dependencies**: yt-dlp, feedparser
- **System dependencies installed on setup**: Node.js, GitHub CLI (`gh`), mcporter
- **MCP layer**: mcporter bridges Exa search into MCP protocol for agent consumption
- **Deployment model**: local-first (desktop/laptop); optional residential proxy (~$1/month) for server deployments accessing geo-blocked platforms (Twitter, Reddit from mainland China)
- **License**: MIT
- **Mirror**: AtomGit (`atomgit.com/qq_51337814/Agent-Reach`) for China-region fast cloning

## Traction [coverage: high — 1 source]

- **30,528 GitHub stars** as of 2026-06-16, approximately four months after the repository was created (2026-02-24) — an exceptionally steep growth curve.
- Last push: 2026-06-12, indicating active maintenance close to the scrape date.
- Explicitly tracked on AtomGit (Chinese Git platform), signaling a significant Chinese developer user base.
- Community WeChat group and Twitter/X account (`@Neo_Reidlab`).
- The README is multilingual (Chinese primary, plus English, Japanese, Korean docs), reflecting international reach.
- Active incident response documented inline: yt-dlp blocked by Bilibili anti-scraping → switched to bili-cli with no user action required; single-platform CLIs deprecated in March 2026 → routes updated.
- Topics indicate cross-platform developer intent: `claude-code`, `cursor`, `mcp`, `free-api`, `llm-tools` alongside platform-specific scrapers.

## Use Cases [coverage: medium — 1 source]

- **AI agent research workflows**: enabling coding agents (Claude Code, Cursor, Windsurf, OpenClaw/Tencent) to autonomously gather internet intelligence — competitor analysis, social sentiment, technical discussions — without paid API subscriptions.
- **Chinese-platform access**: the only tool in this tracker with first-class support for Bilibili, XiaoHongShu, Xueqiu, Xiaoyuzhou, and V2EX alongside Western platforms.
- **Server-side agent pipelines**: deployable on cloud VMs with optional proxy; safe mode for multi-tenant machines.
- **Bootstrapping new agent environments**: the install-by-URL pattern makes onboarding a fresh agent to full internet capability a single-step operation.
- **Cost-constrained setups**: suitable for hobbyist or early-stage projects where Twitter API ($100+/month), Reddit API, or Exa paid tiers are prohibitive.

Not suited for: browser automation, form submission, multi-account management, or parallel headless browser sessions — the README explicitly delineates this boundary and points to BrowserAct for those scenarios.

## Related Frameworks [coverage: medium — 1 source]

- **[BrowserAct](https://browseract.com)**: explicitly recommended as a complement for browser automation tasks Agent-Reach deliberately does not cover (login flows, form submission, multi-session). Supports the same host agents (Claude Code, OpenClaw, Cursor).
- **OpenCLI** (`jackwener/opencli`, 24K stars): a browser-state CLI used as the primary backend for Reddit, XiaoHongShu, and Twitter fallback. Agent-Reach orchestrates it rather than competing with it.
- **Jina Reader** (`jina-ai/reader`): used as Agent-Reach's web-page reading backend and LinkedIn fallback; Agent-Reach adds routing and agent skill registration on top.
- **mcporter** (`nicobailon/mcporter`): MCP bridge used to expose Exa search; Agent-Reach manages its installation and configuration.
- **yt-dlp** (154K stars): bundled as Agent-Reach's YouTube backend; Agent-Reach adds the SKILL.md abstraction so agents invoke it correctly without user instruction per query.
- **Hermes / scraping-focused agent frameworks**: Agent-Reach is narrower — it provides internet read access as a tool layer, not a full agent orchestration pipeline. It is designed to be called *by* agent frameworks, not to replace them.

## Sources [coverage: high — 1 source]

- [[../../sources/github-Panniantong_Agent-Reach]]
