---
topic: lsdefine_genericagent
last_compiled: 2026-07-03
sources:
  - ../../sources/github-lsdefine_GenericAgent
status: active
---

# GenericAgent

## Summary [coverage: low — 1 source]

Scraped 2026-07-03T23:58:07Z. GenericAgent is a minimal, self-evolving autonomous agent framework built around a ~3K-line seed codebase and 9 atomic tools, granting any LLM full system-level control over a local computer including browser, terminal, filesystem, keyboard/mouse, screen vision, and mobile devices via ADB. Its defining characteristic is a self-evolution mechanism: each solved task is automatically crystallized into a reusable Skill stored in a 5-layer memory system, so the agent's capabilities grow organically with use, while keeping token consumption low via a context window capped under 30K tokens. Created in January 2026, it has accumulated 13,281 stars in under six months with daily active development.

## Core Pattern [coverage: low — 1 source]

- Single autonomous execution loop (~100 lines in agent_loop.py): perceive environment state → task reasoning → execute tools → write experience to memory → loop
- 5-layer memory system: L0 Meta Rules, L1 Insight Index, L2 Global Facts, L3 Task Skills/SOPs, L4 Session Archive
- Self-evolution: completed task execution paths are crystallized into reusable Skills saved to L3; future similar tasks invoke the Skill directly via one-line recall
- 9 atomic tools cover all system interaction: code_run, file_read, file_write, file_patch, web_scan, web_execute_js, ask_user, update_working_checkpoint, start_long_term_update
- Dynamic tool creation: agent writes new Python scripts and installs packages at runtime via code_run, promoting temporary abilities to permanent tools

## Key Features [coverage: low — 1 source]

- TMWebdriver: real persistent Chrome/Chromium session (not headless sandbox) preserving login state, cookies, and browser fingerprint — passes major bot-detection checks (56/56 SannySoft, 36/36 incolumitas, reCAPTCHA v3 score 0.9)
- Self-bootstrap proof: the entire repo (git init through every commit) was created autonomously by GenericAgent; author never opened a terminal
- Multi-frontend: Terminal UI (TUI v3, prompt_toolkit/rich), Streamlit web UI, desktop GUI (Windows .exe), IM bots (Telegram, Discord, Lark, WeChat, QQ, WeCom, DingTalk)
- Conductor mode: spawn, supervise, and auto-clean parallel sub-agents (added 2026-05-14)
- Goal Hive mode: BBS-coordinated multi-worker cooperative execution for long-horizon objectives (added 2026-05-17)
- Morphling mode: project-level skill absorption from external repos (added 2026-05-18)
- Token-efficient: claims <30K context vs. 200K–1M for comparable agents; 6x lower token consumption cited
- Published technical report on arXiv (2604.17091); Skill Hub at agentskills.io (Sophub)
- ADB support for Android mobile device control

## Tech Stack [coverage: low — 1 source]

- Primary language: Python 3.11/3.12 (3.14 incompatible due to pywebview)
- Core dependencies minimal: requests, beautifulsoup4, bottle, simple-websocket-server, aiohttp; UI extras via [ui] optional install
- No Playwright, no LangChain, no browser binaries required for base install
- Browser automation: TMWebdriver (Chrome extension + local WebSocket server injecting into real Chrome/Chromium session)
- Model support: Claude, Gemini, Kimi, MiniMax, and others via API key
- Cross-platform: Windows, Linux, macOS; one-line installer scripts for each
- MIT license

## Traction [coverage: low — 1 source]

- 13,281 stars — notable given creation date of 2026-01-16 (under 6 months to scrape)
- Active development: pushed 2026-07-02, one day before scrape
- Technical report published on arXiv 2026-04-21
- Featured by Jiqizhixin (机器之心) 2026-03-01; million-scale Skill Library released 2026-03-10
- Multiple independent community GUIs: ga-manager, galley, A3Agent, GenericAgent-Admin
- DintalClaw: sole authorized commercial partner, a government-affairs bot powered by GenericAgent
- Evaluated against Claude Code and OpenAI CodeX on 5 benchmarks (SOP-Bench, Lifelong AgentBench, RealFin-Benchmark, WebCanvas, BrowseComp-ZH)

## Use Cases [coverage: low — 1 source]

- Personal computer automation where tasks grow more efficient with repeated execution through skill accumulation
- Long-horizon autonomous tasks: stock monitoring, food delivery ordering, expense tracking, bulk messaging
- Browser automation requiring persistent login sessions and CAPTCHA survival (e.g., Discord bot setup)
- Mobile device control via ADB for Android automation workflows
- Long-running goal-directed work via Goal mode or multi-worker Goal Hive mode
- Research and benchmarking: batch trajectory generation for training tool-calling models

## Related Frameworks [coverage: low — 1 source]

- [[nousresearch_hermes-agent]] — also self-evolving with skill creation and persistent memory, but broader deployment (VPS, serverless, messaging gateway); GenericAgent emphasizes OS-level control and token efficiency with a minimal codebase
- [[letta-ai_letta]] — persistent memory platform but API-first and application-embedded; GenericAgent is local-first with autonomous skill growth from a minimal seed
- [[gptme_gptme]] — similar terminal-first personal agent philosophy; gptme has a larger default toolset but no self-evolving skill-tree mechanism
- [[browser-use_browser-harness]] — browser automation specialist; GenericAgent's TMWebdriver approach (real browser injection) contrasts with typical headless automation
- [[significant-gravitas_autogpt]] — early self-directing autonomous agent; much larger codebase and pre-configured architecture vs. GenericAgent's minimal ~3K-line seed approach

## Sources

- [[../../sources/github-lsdefine_GenericAgent]]
