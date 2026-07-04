---
topic: othmanadi_planning-with-files
last_compiled: 2026-07-03
sources:
  - ../../sources/github-OthmanAdi_planning-with-files
status: active
---

# Planning with Files

## Summary [coverage: low — 1 source]

Scraped 2026-07-01T02:48:23Z. Planning with Files is a persistent file-based planning skill for AI coding agents that keeps `task_plan.md`, `findings.md`, and `progress.md` on disk so agents survive context loss, `/clear`, and crashes. It implements the Manus-style "filesystem as memory" pattern — context window as RAM, disk as unlimited persistent storage — with opt-in autonomous and gated completion modes added in v3.0. At 24,197 stars and version 3.1.3, it is one of the most widely adopted Claude Code skills, installable across 60+ agents via the SKILL.md standard.

## Core Pattern [coverage: low — 1 source]

- Three-file planning pattern: `task_plan.md` (phases/progress), `findings.md` (research), `progress.md` (session log/errors)
- Hook-driven re-injection: PreToolUse hook re-reads the plan before major decisions; autonomous mode injects at session start and phase transitions instead
- Completion gate: Stop hook blocks agent exit until all plan phases are verified done (gated mode only)
- Append-only JSONL run ledger replaces raw `progress.md` tail in v3 modes for structured summaries
- Multi-agent parallel plan isolation: `.planning/YYYY-MM-DD-slug/` directories with session attachment gating
- SHA-256 hash attestation (`attest-plan.sh`) locks `task_plan.md` against tampering; hooks block injection on mismatch

## Key Features [coverage: low — 1 source]

- SKILL.md open standard — one `npx skills add` installs across Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, Kiro, Mastra Code, Hermes Agent, and 17+ other platforms
- Session recovery: after `/clear`, skill auto-reads previous session from IDE session store and shows catchup report
- Three execution modes: legacy (per-tool re-inject), autonomous (session-start + phase-transition), gated (completion-blocking stop hook)
- 96.7% benchmark pass rate on file-pattern fidelity (v2.21.0, claude-sonnet-4-6, 30 assertions, 10 parallel subagents)
- Six language variants: English, Arabic, German, Spanish, Chinese Simplified, Chinese Traditional
- Plugin commands: `/plan-goal` (derives termination condition), `/plan-loop` (10-minute tick with plan re-read), `/plan-attest`

## Tech Stack [coverage: low — 1 source]

- Primary language: Python (scripts and test suite); shell scripts for hooks (POSIX-portable)
- Claude Code plugin + SKILL.md standard for cross-IDE installation
- Hook scripts in both bash and PowerShell for Windows parity
- Test suite: 184+ pytest assertions covering YAML frontmatter, script permissions, session slug logic, hook lifecycle
- Installation: `npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g`

## Traction [coverage: low — 1 source]

- 24,197 stars; viral growth (blew up within 24 hours of initial release)
- Last pushed: 2026-06-16; very active release cadence (v3.1.3 at time of scrape)
- Active community: forks extended into multi-project, multi-level cascade, and crowdfunding-for-agents workflows
- Referenced in finance agent frameworks and Claude Code harness projects
- Listed in bilingual skill hubs indexing 31,000+ Claude Code skills

## Use Cases [coverage: low — 1 source]

- Long-running coding sessions that span multiple context windows or `/clear` operations
- Multi-step research and build tasks (3+ steps) where goal drift is a risk
- Multi-agent collaborative work where shared disk state replaces context sharing
- Autonomous agent runs requiring deterministic completion verification
- Any agent platform supporting SKILL.md that needs persistent, crash-proof execution state

## Related Frameworks [coverage: low — 1 source]

- [[nousresearch_hermes-agent]] — explicit integration documented in `docs/hermes.md`; planning-with-files ships a Hermes-specific SKILL.md adapter
- [[ruvnet_ruflo]] — another Claude Code harness/meta-framework; ruflo adds swarm coordination and memory layers while planning-with-files focuses on file-based execution state
- [[microsoft_autogen]] — complementary: AutoGen provides multi-agent orchestration while planning-with-files provides the per-agent planning continuity layer
- [[letta-ai_letta]] — Letta addresses agent memory recall from past sessions; planning-with-files addresses active execution-state continuity during the current task
- [[significant-gravitas_autogpt]] — AutoGPT is a full autonomous agent platform; planning-with-files is a lightweight skill that can augment any coding agent without replacing its orchestration layer

## Sources

- [[../../sources/github-OthmanAdi_planning-with-files]]
