---
topic: rightnow-ai_openfang
last_compiled: 2026-07-03
sources:
  - ../../sources/github-RightNow-AI_openfang
status: active
---

# OpenFang

## Summary [coverage: low — 1 source]

Scraped 2026-07-03T23:58:19Z. OpenFang is an open-source Agent Operating System built from scratch in Rust — 137,728 lines of code across 14 crates — that compiles to a single ~32 MB binary. Unlike chatbot frameworks, it runs autonomous agents ("Hands") on schedules without waiting for user prompts, covering use cases like competitor intelligence, lead generation, social media management, and deep research. At 17,962 stars and pre-1.0 (v0.6.9), it is actively developed with an ambitious security model (16 discrete security systems) and broad channel support (40 messaging adapters).

## Core Pattern [coverage: low — 1 source]

- "Hands" abstraction: pre-built autonomous capability packages that run independently on schedules with multi-phase operational playbooks (500+ word system prompts)
- Each Hand bundles: `HAND.toml` manifest (tools, settings, requirements, dashboard metrics), system prompt, `SKILL.md` domain reference, and approval guardrails
- Kernel + runtime architecture: `openfang-kernel` handles orchestration/scheduling/RBAC; `openfang-runtime` handles the agent loop, LLM drivers, tools, and WASM sandbox
- WASM dual-metered sandbox: tool code runs in WebAssembly with fuel metering + epoch interruption; watchdog thread kills runaway code
- Merkle hash-chain audit trail: every action cryptographically linked to the previous one
- OpenAI-compatible API: 140+ REST/WS/SSE endpoints; drop-in replacement for existing tooling

## Key Features [coverage: low — 1 source]

- 7 bundled Hands: Clip (YouTube shorts pipeline), Lead (daily prospect discovery and scoring), Collector (OSINT continuous monitoring), Predictor (superforecasting with Brier scores), Researcher (deep cross-referenced research), Twitter (autonomous account management with approval queue), Browser (Playwright-based web automation with mandatory purchase approval gate)
- 16 security systems: WASM sandbox, Merkle audit trail, taint tracking, Ed25519 signed manifests, SSRF protection, secret zeroization, GCRA rate limiter, prompt injection scanner, loop guard, and more
- 40 channel adapters: Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Teams, Mastodon, Bluesky, and 31 others
- 27 LLM providers / 123+ models via 3 native drivers (Anthropic, Gemini, OpenAI-compatible)
- Tauri 2.0 native desktop app with system tray and global shortcuts
- Migration engine: import agents, memory, skills, and config from OpenClaw, LangChain, AutoGPT
- FangHub marketplace for community-published Hands
- SQLite + vector memory with canonical sessions and compaction

## Tech Stack [coverage: low — 1 source]

- Primary language: Rust (14 crates, 137K LOC, zero clippy warnings, 2,696+ tests)
- Deployment: single ~32 MB binary; one-line curl install
- Desktop: Tauri 2.0 (cross-platform native app)
- Memory: SQLite persistence + vector embeddings
- Sandbox: WASM with dual metering
- P2P: OFP protocol with HMAC-SHA256 mutual authentication
- Credential vault: AES-256-GCM with OAuth2 PKCE

## Traction [coverage: low — 1 source]

- 17,962 stars; created 2026-02-24 (~4 months to ~18k stars — rapid growth)
- Last pushed: 2026-07-02; very active development (shipping fast, fixing fast per README)
- Pre-1.0 (v0.6.9 at scrape time); breaking changes expected between minor versions until v1.0
- Discord community; target: stable v1.0 by mid-2026

## Use Cases [coverage: low — 1 source]

- Autonomous background agents running on schedules without user prompting (competitor monitoring, lead gen, social media management)
- High-security agentic deployments requiring deep defense-in-depth (16 security layers)
- Organizations migrating from OpenClaw, LangChain, or AutoGPT (built-in migration engine)
- Teams needing 40+ messaging channel adapters with per-channel model overrides
- Researchers and OSINT practitioners needing continuous monitoring with knowledge graph construction

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — AutoGen focuses on multi-agent conversation orchestration in Python; OpenFang is a full autonomous OS in Rust with scheduled execution and a broader channel/security surface
- [[significant-gravitas_autogpt]] — AutoGPT is the original autonomous agent platform (Python, 185k stars); OpenFang explicitly provides an AutoGPT migration engine and benchmarks against it, positioning itself as a more performant alternative
- [[letta-ai_letta]] — Letta specializes in long-term agent memory; OpenFang includes SQLite + vector memory as one component of a broader OS-level architecture
- [[camel-ai_camel]] — CAMEL is a Python research framework for role-playing agents; OpenFang is production-oriented, Rust-based, and focused on autonomous scheduled execution
- [[google_adk-python]] — ADK is Google's Python agent framework targeting Gemini-centric cloud workflows; OpenFang supports 27 providers including Gemini with broader channel and security depth

## Sources

- [[../../sources/github-RightNow-AI_openfang]]
