---
topic: evomap_evolver
last_compiled: 2026-07-03
sources:
  - ../../sources/github-EvoMap_evolver
status: active
---

# Evolver

## Summary [coverage: low — 1 source]

Scraped 2026-06-16T03:10:33Z. Evolver is a GEP (Genome Evolution Protocol)-powered self-evolution engine for AI agents, built by EvoMap. It turns ad hoc prompt tweaks into auditable, reusable evolution assets (Genes, Capsules, EvolutionEvents) and emits protocol-bound GEP prompts that guide incremental agent improvement rather than directly patching code. The project is transitioning from GPL-3.0 open source to a source-available model due to alleged design appropriation by a competing project; previously-published versions remain freely usable under their original terms. Research backing comes from arXiv:2604.15097, which shows Gene-based representations outperform Skill documents across 4,590 controlled trials.

## Core Pattern [coverage: low — 1 source]

- **Prompt generator, not code patcher:** each cycle scans `memory/` for runtime logs and error signals, selects a matching Gene or Capsule from a local GEP asset store, and emits a structured GEP prompt to stdout — no source code is touched autonomously.
- **GEP asset store:** Genes and Capsules live in `<workspace>/.evolver/gep/`; EvolutionEvents are appended to `events.jsonl` for a full audit trail.
- **Strategy presets:** `EVOLVE_STRATEGY=balanced|innovate|harden|repair-only` controls the mix of innovation, optimization, and repair intent per cycle.
- **Host runtime integration:** stdout directives (`sessions_spawn(...)`) can be consumed by compatible runtimes (OpenClaw, Cursor, Claude Code, Codex, Kiro, opencode) via `evolver setup-hooks --platform=<name>`; in standalone mode they are plain text output.
- **Optional EvoMap Hub:** offline by default; connecting unlocks skill sharing, a worker pool, evolution leaderboards, and a decentralized validator role (earn credits by validating other nodes' evolution claims).

## Key Features [coverage: low — 1 source]

- Auto-log analysis: scans memory and history files for errors and patterns
- Self-repair guidance: emits repair-focused directives from detected signals
- Mutation + Personality Evolution: each run is gated by an explicit Mutation object and an evolvable PersonalityState
- Signal de-duplication: detects stagnation patterns to prevent repair loops
- Configurable strategy presets (`balanced`, `innovate`, `harden`, `repair-only`)
- Operations module (`src/ops/`): portable lifecycle management, skill monitoring, cleanup, self-repair, wake triggers — zero platform dependency
- Skill Store: download and publish reusable skills via `evolver fetch --skill <id>` (requires Hub connection)
- Protected source files: prevents autonomous agents from overwriting core evolver code
- Review mode (`--review`): human-in-the-loop confirmation before applying each evolution step
- Auto GitHub issue reporting: files sanitized issue reports on persistent failure loops (opt-out via `EVOLVER_AUTO_ISSUE=false`)
- GEPX bundle export: `evolver sync --scope=all --export=backup.gepx` recovers Hub-published assets after local store loss
- A2A external asset ingestion with staged promotion and safety checks before Gene/Capsule hits local store
- Decentralized validator role when connected to EvoMap Hub (periodic validation tasks, consensus credits)

## Tech Stack [coverage: low — 1 source]

- **Language:** JavaScript (Node.js >= 18); core engine modules distributed in obfuscated form
- **Distribution:** npm (`@evomap/evolver`), GitHub Releases binaries, ClawHub skill registry
- **License:** GPL-3.0-or-later (transitioning to source-available for future releases)
- **Key dependencies:** Git (required — used for rollback, blast radius calculation, solidify); dotenv; optional Hub connection via A2A protocol
- **Deployment:** CLI (`evolver` / `node index.js`); daemon via `--loop` or pm2/cron keepalive; integrates into Cursor, Claude Code, Codex, Kiro, opencode, OpenClaw via `setup-hooks`
- **Research basis:** arXiv:2604.15097 — Gene representation outperforms Skill docs for iterative experience accumulation across 4,590 controlled trials

## Traction [coverage: low — 1 source]

- **Stars:** 8,696
- **Last push:** 2026-06-15
- **Created:** 2026-02-01
- Active community with 10+ named contributors across bug fixes, multilingual signal extraction, security hardening, and documentation
- Multi-language README: English, Chinese, Japanese, Korean
- Published research paper (arXiv:2604.15097) validating the Gene-over-Skills approach
- Promoted on XiaoHongShu; author notes concern about design appropriation by a competing project

## Use Cases [coverage: low — 1 source]

- Hardening flaky agent loops by enforcing validation before edits are applied
- Encoding recurring fixes as reusable Genes and Capsules for future evolution cycles
- Producing auditable EvolutionEvent trails for compliance or review workflows
- Teams maintaining agent prompts and logs at scale who need deterministic, protocol-bound changes
- Environments requiring human-in-the-loop review of each evolution step (`--review` mode)
- Background self-maintenance of long-running agent processes (`--loop` daemon mode)

## Related Frameworks [coverage: low — 1 source]

- [[nousresearch_hermes-agent]] — general-purpose agentic CLI; Evolver's README notes alleged design similarity to Evolver's memory/skill/evolution-asset system without attribution
- [[microsoft_autogen]] — multi-agent orchestration framework; Evolver is a single-agent self-evolution engine focused on auditable prompt governance rather than multi-agent coordination
- [[letta-ai_letta]] — persistent memory and stateful agents; Evolver similarly accumulates experience (as Genes/Capsules) but frames it as a governance protocol rather than a memory database
- [[significant-gravitas_autogpt]] — autonomous agent with goal decomposition; Evolver is narrower, acting as a prompt-generation layer that guides a host agent rather than acting as the agent itself
- [[cft0808_edict]] — also runs on OpenClaw as host runtime; Edict provides multi-agent institutional orchestration while Evolver provides self-evolution prompt governance for individual agents

## Sources

- [[../../sources/github-EvoMap_evolver]]
