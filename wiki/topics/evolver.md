---
topic: evolver
last_compiled: 2026-06-29
source_count: 1
status: active
---

# Evolver (EvoMap)

## Summary [coverage: high — 1 source]

Evolver is a GEP-powered (Genome Evolution Protocol) self-evolution engine for AI agents, built by EvoMap. Its core value proposition is turning ad hoc prompt tweaks into auditable, reusable evolution assets — Genes, Capsules, and EvolutionEvents — under a protocol-constrained model. Rather than patching code, it generates structured GEP prompts that guide the next evolution step of a host agent, then records an immutable audit trail.

Source scraped: 2026-06-16T03:10:33Z. The repo was created 2026-02-01 and last pushed 2026-06-15, making it a very recent framework (under 5 months old at scrape time). Note: the project is transitioning from GPL-3.0 open source to a source-available license, citing an IP dispute with a project (Hermes Agent) that allegedly copied Evolver's memory/skill/evolution-asset design without attribution.

## Core Pattern [coverage: high — 1 source]

Evolver is not an orchestrator or multi-agent runner — it is a **prompt generator and evolution loop engine**. Each cycle:

1. Scans `./memory/` for runtime logs, error patterns, and signals.
2. Selects the best-matching Gene or Capsule from the local GEP asset store (`<workspace>/.evolver/gep/`).
3. Emits a protocol-bound GEP prompt to stdout that guides the next evolution step.
4. Records an `EvolutionEvent` (append-only `.jsonl`) for auditability.

The core abstractions are:
- **Gene**: a compact, reusable representation of accumulated agent experience. Research (arXiv:2604.15097, 4,590 controlled trials) shows Gene representations outperform documentation-style Skill packages in stability and iterative accumulation.
- **Capsule**: another evolution asset type that can be selected alongside Genes.
- **EvolutionEvent**: immutable audit record of each evolution step.
- **Mutation object**: gates every evolution run, making changes explicit and controlled.
- **PersonalityState**: an evolvable state that drifts over cycles.
- **Strategy presets**: `balanced` (default), `innovate`, `harden`, `repair-only` — control the weighting between new features, optimization, and repair.

Evolver does not orchestrate multiple agents or manage workflows. It is designed to be invoked **from within** a host agent runtime (OpenClaw, Cursor, Claude Code, Codex, Kiro, opencode) or run standalone via CLI. It never modifies source code directly.

## Key Features [coverage: high — 1 source]

- **GEP Protocol**: standardized, protocol-constrained evolution with structured asset store (genes.json, capsules.json, events.jsonl). Asset store is never overwritten on upgrades.
- **MCP support**: listed as a first-class topic; integrates with MCP clients via a Proxy mailbox API documented in SKILL.md.
- **Hook integrations**: `evolver setup-hooks --platform=<platform>` wires Evolver into Cursor, Claude Code, Codex, Kiro, and opencode lifecycle hooks.
- **Offline-capable**: all core evolution features work fully locally with no internet connection.
- **EvoMap Hub (optional)**: connects to `evomap.ai` for skill store, worker pool, evolution leaderboards, evolution circles, and asset publishing.
- **Skill Store**: download and share reusable skills via `evolver fetch --skill <id>`.
- **Worker Pool**: opt-in distributed task execution across the EvoMap network (`WORKER_ENABLED=1`).
- **Decentralized Validator role**: nodes connected to the hub can validate other nodes' evolution claims and earn credits/reputation.
- **Signal de-duplication**: detects stagnation patterns to prevent repair loops.
- **Security model**: Gene validation commands are whitelisted to `node`/`npm`/`npx` only; no shell operators, no command substitution; 180-second timeout. External assets require explicit promotion with `--validated` flag.
- **Auto GitHub Issue Reporting**: files sanitized bug reports upstream on persistent failure streaks.
- **A2A protocol**: agent-to-agent protocol support for networked collaboration.
- **Multilingual docs**: Chinese, Japanese, Korean READMEs.
- **CLI modes**: single run, `--review` (human-in-the-loop), `--loop` (background daemon).

## Tech Stack [coverage: high — 1 source]

- **Primary language**: JavaScript
- **Runtime**: Node.js >= 18
- **Package**: `npm install -g @evomap/evolver` (`@evomap/evolver` on npm)
- **Git dependency**: required at runtime — used for rollback, blast radius calculation, and solidify operations. Must run inside a git-initialized directory.
- **Deployment**: CLI tool; also ships prebuilt binaries on GitHub Releases and the ClawHub skill registry.
- **License**: GPL-3.0-or-later (transitioning to source-available; core evolution engine modules are already shipped in obfuscated form).
- **Research basis**: arXiv:2604.15097 — "From Procedural Skills to Strategy Genes: Towards Experience-Driven Test-Time Evolution."
- **Config**: `.env` file per project for hub credentials and strategy; environment variables for all runtime tuning.

## Traction [coverage: high — 1 source]

- **8,696 stars** — strong for a repo under 5 months old (created 2026-02-01).
- **Actively maintained**: last pushed 2026-06-15 (one day before scrape), indicating very active development.
- **Community**: 15+ named contributors with substantive PRs (bug fixes, test coverage at 45 tests, credential redaction hardening, multilingual signal extraction, CPU load threshold auto-calculation).
- **International reach**: Chinese, Japanese, and Korean documentation; contributor base appears global.
- **Research-backed**: accompanying arXiv paper with 4,590 controlled trials on 45 scientific code-solving scenarios.
- **Distribution channels**: npm, GitHub Releases, and ClawHub skill registry.
- **Ecosystem signals**: EvoMap network platform with leaderboards and worker pools; OpenClaw natively integrates Evolver stdout directives without setup.
- **Concern**: license direction is uncertain — moving toward source-available due to IP disputes, and core modules are already obfuscated. This may affect long-term open-source adoption.

## Use Cases [coverage: high — 1 source]

Best suited for:
- Teams maintaining agent prompts and logs at scale who need reproducible, auditable evolution rather than ad hoc prompt edits.
- Compliance or regulated environments requiring immutable evolution traces.
- Hardening flaky agent loops by enforcing protocol-bound validation before changes are applied.
- Encoding recurring fixes or behaviors as reusable Genes and Capsules that can be shared via the EvoMap network.
- Agents embedded in supported runtimes (OpenClaw, Cursor, Claude Code, Codex, Kiro, opencode) that should self-improve between sessions.
- Research use cases evaluating gene-based vs. skill-based experience accumulation in LLM agents.

Not suited for:
- One-off scripts without runtime logs or history.
- Projects requiring free-form or creative autonomous changes.
- Systems with zero tolerance for protocol overhead.
- Environments that need a traditional multi-agent orchestrator or workflow engine.

## Related Frameworks [coverage: medium — 1 source]

- **OpenClaw**: the closest native integration partner — OpenClaw agents interpret Evolver's `sessions_spawn(...)` stdout directives without any additional setup. Positioned as the primary host runtime for Evolver.
- **Hermes Agent (NousResearch)**: a competing project cited in the README as having allegedly copied Evolver's memory/skill/evolution-asset design. The IP dispute is what's driving the license change to source-available.
- **Cursor / Claude Code / Codex / Kiro / opencode**: supported host runtimes via the `setup-hooks` command — Evolver is wired into their session lifecycle hooks, not a competitor to these tools.
- **Skill-based agent frameworks (general)**: Evolver explicitly positions Genes as superior to documentation-style Skill packages (its own research claim) for experience accumulation — frameworks relying on RAG-style skill docs sit in contrast.
- **A2A protocol ecosystem**: Evolver implements the A2A (agent-to-agent) protocol for networked collaboration, placing it within the broader A2A-compatible agent ecosystem.

## Sources [coverage: high — 1 source]

- [[../../sources/github-EvoMap_evolver]]
