---
topic: GenericAgent
last_compiled: 2026-06-29
source_count: 1
status: active
---

# GenericAgent

## Summary [coverage: high — 1 sources]

GenericAgent is a minimal, self-evolving autonomous agent framework from `lsdefine/GenericAgent`. Its core value proposition is that the entire framework is just ~3,000 lines of seed code and a ~100-line Agent Loop, yet grants any LLM system-level control over a local computer — covering browser, terminal, filesystem, keyboard/mouse input, screen vision, and mobile devices (via ADB). The central design philosophy is "don't preload skills, evolve them": every time the agent solves a new task it automatically crystallizes the execution path into a reusable Skill, growing a personal skill tree over time. The project claims 6x lower token consumption than comparable agents by keeping its context window under 30K tokens, compared to the 200K–1M windows other agents consume.

The project has a technical report on arXiv (arxiv.org/abs/2604.17091): "GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization". Official website: gaagent.ai.

Source scraped: 2026-06-16T03:10:29Z.

## Core Pattern [coverage: high — 1 sources]

GenericAgent's architecture combines three primitives: **Layered Memory x Minimal Toolset x Autonomous Execution Loop**.

**Execution loop:** Perceive environment state → Task reasoning → Execute tools → Write experience to memory → Loop. The loop is implemented in ~100 lines in `agent_loop.py`.

**5-layer memory system:**
- L0 — Meta Rules: core behavioral rules and system constraints
- L1 — Insight Index: minimal memory index for fast routing and recall
- L2 — Global Facts: stable knowledge accumulated over long-term operation
- L3 — Task Skills / SOPs: reusable workflows for specific task types
- L4 — Session Archive: archived task records distilled from finished sessions for long-horizon recall

**Self-evolution mechanism:** When the agent encounters a new task it explores autonomously (installs deps, writes scripts, debugs), then crystallizes the successful execution path into a Skill written to L3. On subsequent similar tasks it invokes the Skill directly rather than re-exploring. This compounds: after weeks of use an agent instance builds a skill tree unique to its owner and usage patterns.

**Special execution modes added post-launch:**
- Goal mode (`reflect/goal_mode.py`, 2026-05-08): time-budget-driven self-driven loop — runs until a time budget expires rather than delivering prematurely
- Goal Hive mode (2026-05-17): multi-worker cooperative Goal mode with BBS-coordinated master/worker parallelism for long-horizon objectives
- Conductor (2026-05-14): sub-agent orchestration — spawn, supervise, and auto-clean parallel sub-agents
- Morphling mode (2026-05-18): project-level skill absorption — extract goal and tests from any external repo, then decide per component whether to call, rewrite, or discard it

## Key Features [coverage: high — 1 sources]

**Self-evolving skill tree:** Each completed task writes a reusable Skill to memory. No manual plugin authoring required; capabilities accumulate automatically with usage.

**Real browser control via TMWebdriver:** A local WebSocket server plus a Chrome extension that injects into a real, persistent Chrome/Chromium session rather than a disposable headless sandbox. Preserves login state, cookies, extensions, GPU/WebGL behavior, and normal session fingerprints. Demonstrated passing hCaptcha challenges mid-task. Evaluation: 56/56 SannySoft headless tests passed, 36/36 bot.incolumitas.com checks passed, reCAPTCHA v3 human-like score of 0.9.

**System-level OS control:** Mouse and keyboard input, screen vision (OCR + vision LLM), ADB for Android device control.

**Minimal dependencies:** Core requires only `requests` plus four lightweight packages for TMWebdriver's local server. No Playwright, no LangChain, no browser binaries to download by default. Advanced capabilities (OCR, vision, computer-use) are unlocked by instructing the agent to self-configure — it reads pre-installed SOPs from its memory layer and installs what is needed.

**Multi-model support:** Claude, Gemini, Kimi (Moonshot), MiniMax. Cross-platform (Windows, Linux, macOS; macOS/Linux get platform-equivalent input/screenshot tools via the same self-adaptation mechanism).

**Multiple frontends:**
- TUI v3 (`frontends/tui_v3.py`): Terminal UI built on `prompt_toolkit` + `rich`, multi-session, real-time streaming
- Streamlit web UI (`launch.pyw`)
- Desktop GUI (`frontends/GenericAgent.exe`) — shipped in one-line installer
- IM bots: Telegram, Discord, Lark/Feishu, WeChat, QQ, WeCom, DingTalk

**Token efficiency:** <30K context window by design. Claims less noise, fewer hallucinations, higher success rate, and lower cost compared to agents running in 200K–1M windows.

## Tech Stack [coverage: high — 1 sources]

- **Primary language:** Python (requires 3.11 or 3.12; incompatible with 3.14 due to `pywebview`)
- **Installation:** `pip install -e ".[ui]"` via `uv`; one-line installer scripts for Windows (PowerShell) and Linux/macOS
- **Core dependencies:** `requests`, `beautifulsoup4`, `bottle`, `simple-websocket-server`, `aiohttp`
- **UI extras:** `streamlit`, `prompt_toolkit`, `rich`
- **Browser automation:** TMWebdriver (custom local WebSocket server + Chrome extension — no Playwright, no Selenium)
- **Deployment:** Local, self-hosted. API key for LLM backend required. No cloud service dependency beyond the LLM provider.
- **License:** MIT

## Traction [coverage: high — 1 sources]

- **Stars:** 12,890 as of scrape date (2026-06-16)
- **Created:** 2026-01-16 (V1.0 public release)
- **Last pushed:** 2026-06-16 — actively maintained with frequent feature releases
- **arXiv technical report** published 2026-04-21
- **Skill Hub:** Sophub (fudankw.cn/sophub) — community-contributed skill library; a million-scale Skill Library released 2026-03-10
- **Media coverage:** Featured by Jiqizhixin (机器之心), a major Chinese AI media outlet, 2026-03-01
- **Commercial deployment:** DintalClaw — officially authorized commercial partner, released as a government-affairs bot 2026-03-08
- **Community GUIs (independent OSS):**
  - `chilishark27/ga-manager`
  - `wangjc683/galley` — out-of-the-box local agent workbench with bundled CPython 3.11 runtime, multi-session + Project orchestration
  - `FroStorM/A3Agent`
  - `Fwind43/GenericAgent-Admin` — Go + React desktop admin panel with service lifecycle management, Goal mode, BBS team board, TMWebDriver monitor, and Windows tray/desktop-pet integration
- **Tutorial:** Datawhale community tutorial at datawhalechina.github.io/hello-generic-agent
- **Community:** LinuxDo community; WeChat group (group 21 active as of scrape)
- **Reproduction repo:** JinyiHan99/GA-Technical-Report with full evaluation datasets and results
- **Trendshift:** Listed on trendshift.io/repositories/25944

## Use Cases [coverage: high — 1 sources]

GenericAgent is best suited for local computer automation tasks that benefit from accumulating skills over time rather than being re-solved from scratch each run. Demonstrated use cases from the README:

- **Web automation:** Real-browser session tasks including CAPTCHA-surviving login flows, autonomous web exploration and summarization, Discord bot configuration
- **Financial/quantitative:** Stock screening with quantitative conditions (EXPMA golden cross, turnover filters), expense tracking via Alipay ADB
- **Messaging automation:** Batch WeChat messaging, reading WeChat message history via reverse-engineered DB
- **General personal automation:** Food delivery ordering, Gmail sending with OAuth setup, Hacker News morning digest with cron scheduling, stock monitoring with alert cron
- **Long-horizon objectives:** Goal Hive mode for multi-hour/multi-worker optimization tasks
- **Project-level code absorption:** Morphling mode for extracting and selectively rewriting components from external repositories

It is particularly well-matched for users who want a low-overhead local agent that gets more capable through use rather than through upfront configuration, and for tasks requiring real browser sessions where cookie/login persistence matters.

## Related Frameworks [coverage: medium — 1 sources]

The README provides an explicit comparison table:

**OpenClaw**
- ~530,000 lines vs GenericAgent's ~3K
- Multi-service orchestration deployment vs `pip install` + API key
- Sandbox/headless browser vs real persistent browser session
- Multi-agent delegation for OS control vs direct mouse/keyboard/ADB
- Plugin ecosystem for capability extension vs autonomous skill growth
- No observed cross-task self-evolution convergence in GenericAgent's evaluation

**Claude Code**
- Large open-sourced codebase vs ~3K seed
- CLI + subscription vs pip install + LLM API key
- Browser control via MCP plugin vs native TMWebdriver
- File + terminal OS control vs full keyboard/mouse/vision/ADB
- Stateless between sessions vs persistent evolving skill tree
- Used as a baseline in GenericAgent's evaluation suite

GenericAgent's differentiation is primarily the self-evolution mechanism and the real-browser approach — both absent from stateless CLI agents. It occupies the "minimal local agent" niche versus heavier multi-service orchestration frameworks.

## Sources [coverage: high — 1 sources]

- [[../../sources/github-lsdefine_GenericAgent]]
