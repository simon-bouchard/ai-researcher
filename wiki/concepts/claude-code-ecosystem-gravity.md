---
concept: Claude Code Ecosystem Gravity
last_compiled: 2026-07-04
topics_connected: [gitlawb_openclaude, cft0808_edict, evomap_evolver, nousresearch_hermes-agent, yeachan-heo_oh-my-claudecode, ruvnet_ruflo, rightnow-ai_openfang, othmanadi_planning-with-files, panniantong_agent-reach, jackwener_opencli, duckbugio_flock, omnigent-ai_omnigent, forsy-ai_agent-apprenticeship]
status: active
---

# Claude Code Ecosystem Gravity

## Pattern

Claude Code and its precursor OpenClaw have become a gravitational center for the agent ecosystem — 13 of the 40 tracked frameworks are either forks of, harnesses around, skills for, migration sources from, or wrappers around this single tool. This is a non-obvious structural fact: a developer tool designed to assist one engineer at a time has generated a secondary ecosystem of frameworks that coordinate multiple agents, extend its capabilities, and adapt it for new audiences. The ecosystem is stratified into five layers, each representing a different kind of "gravity":

1. **Forks** (OpenClaude): take the Claude Code codebase and extend it with new features (multi-provider, headless gRPC, background sessions)
2. **Harnesses** (Ruflo, oh-my-claudecode, Edict): sit above Claude Code and add orchestration, swarm coordination, team pipelines, or institutional review on top
3. **Skills/extensions** (Planning with Files, Agent Reach, OpenCLI): install capabilities into Claude Code via the SKILL.md standard without replacing the agent itself
4. **Migration paths** (Hermes, OpenFang): offer `hermes claw migrate` or an OpenClaw import engine, acknowledging that a significant user base has Claude Code/OpenClaw history to preserve
5. **Single-purpose products built entirely on Claude Code** (Flock) and **meta-harnesses/learning layers that treat Claude Code as one first-class backend among several** (Omnigent, Agent Apprenticeship): a newer pattern where Claude Code is no longer just a codebase to fork or extend, but a stable enough runtime that whole products assume it as infrastructure

## Instances

- **2026-07-02** in [[../topics/gitlawb_openclaude]]: Direct fork of Claude Code codebase, extended with multi-provider routing, headless gRPC mode, and background sessions. 29,654 stars in ~3 months — the fork has its own traction.
- **2026-07-03** in [[../topics/ruvnet_ruflo]]: Explicit meta-harness: "Agent = Model + Harness; Ruflo is the harness" — wraps Claude Code and Codex; 35 Claude Code plugins; 62,853 stars.
- **2026-07-01** in [[../topics/yeachan-heo_oh-my-claudecode]]: Teams-first orchestration layer built on Claude Code; staged pipeline (plan → PRD → exec → verify → fix); tmux workers extending to Codex, Gemini, Grok, Cursor; 37,282 stars.
- **2026-06-22** in [[../topics/cft0808_edict]]: Requires OpenClaw as its underlying runtime; adds 12-agent institutional orchestration, mandatory review pipeline, and real-time dashboard. OpenClaw is the "OS" that Edict runs on.
- **2026-06-15** in [[../topics/evomap_evolver]]: Integrates with Claude Code, Codex, Cursor, Kiro, opencode, OpenClaw via `evolver setup-hooks --platform=<name>` — targets Claude Code as the primary deployment context for its GEP self-evolution engine.
- **2026-07-03** in [[../topics/nousresearch_hermes-agent]]: `hermes claw migrate` imports settings, memories, skills, API keys, and workspace instructions from OpenClaw — explicit migration tooling acknowledging an installed OpenClaw user base.
- **2026-07-03** in [[../topics/rightnow-ai_openfang]]: Built-in migration engine importing agents, memory, skills, and config from OpenClaw, LangChain, and AutoGPT — treats OpenClaw migration as a table-stakes feature for user acquisition.
- **2026-07-01** in [[../topics/othmanadi_planning-with-files]]: One of the most-starred Claude Code skills (24,197 stars); SKILL.md open standard that installs across 60+ agents; defines the file-based planning pattern now referenced across the ecosystem.
- **2026-06-12** in [[../topics/panniantong_agent-reach]]: Capability layer installable in Claude Code, Cursor, OpenClaw, Windsurf, Codex, and any shell-capable agent; positions Claude Code as the primary target audience.
- **2026-06-15** in [[../topics/jackwener_opencli]]: Skills installable into Claude Code, Cursor, and other skill-aware agents; skill format explicitly compatible with the Claude Code skill system.
- **2026-07-02** in [[../topics/duckbugio_flock]]: Entire product is a chat-driven dev-team pipeline built on native Claude Code subagents (`core/agents/`); runs on a Claude Pro/Max subscription or Anthropic API key; has no non-Claude-Code execution path at all — the deepest dependency in the tracked set.
- **2026-07-04** in [[../topics/omnigent-ai_omnigent]]: Meta-harness treating Claude Code as one of six first-class wrapped harnesses (`claude-sdk`/`claude-native` alongside Codex, Cursor, OpenCode, Hermes, Pi); example agent "Polly" specifically delegates coding sub-tasks to Claude Code among others and cross-vendor-reviews the diffs.
- **2026-07-03** in [[../topics/forsy-ai_agent-apprenticeship]]: Lists Claude Code as one of seven auto-detected "Apprentice Agents" whose task executions become reusable Experience Compilations — treats Claude Code as a pluggable execution backend for learning-signal extraction rather than something to fork or extend.

## What This Means

Claude Code has achieved something rare: it has become a *platform* with genuine ecosystem effects, not just a tool. The evidence is the secondary market — frameworks, harnesses, and skill marketplaces that exist specifically because Claude Code does. This is the same dynamic that made VS Code dominant: once a developer tool reaches critical mass, third-party extensions and integrations create lock-in that has nothing to do with the core product.

The SKILL.md standard is particularly significant. Planning with Files (24k stars) established a skill format that "installs across 60+ agents." If this standard consolidates, it creates a portable skill layer that works across Claude Code, Cursor, Codex, and others — reducing the lock-in while keeping Claude Code as the reference implementation.

The OpenClaw connection reveals a succession pattern: OpenClaw was the earlier community agent runtime; Hermes and OpenFang both offer explicit migration tooling *away* from it. This suggests OpenClaw is losing to Hermes/OpenFang as the default "community agent runtime" — but both new entrants chose to honor the migration rather than break it, because the OpenClaw user base was real.

The structural risk: this gravity is real but fragile. If Anthropic changes the Claude Code architecture or licensing in ways that break the ecosystem (as has happened with other dev tools), the 13 frameworks that depend on it would be affected simultaneously.

The newest layer (Flock, Omnigent, Agent Apprenticeship — all scraped 2026-07-02 to 2026-07-04) marks a maturity shift: earlier entrants either forked Claude Code or extended it in place; these three instead build *around* it as a stable dependency, no different in kind from depending on a cloud API. Flock goes furthest — it has no non-Claude-Code code path at all, betting the entire product on Claude Code's subscription model remaining available and priced as-is. Omnigent and Agent Apprenticeship hedge by treating Claude Code as one interchangeable backend among several, which is the more defensible position given the structural risk noted above.

## Sources

- [[../topics/gitlawb_openclaude]]
- [[../topics/cft0808_edict]]
- [[../topics/evomap_evolver]]
- [[../topics/nousresearch_hermes-agent]]
- [[../topics/yeachan-heo_oh-my-claudecode]]
- [[../topics/ruvnet_ruflo]]
- [[../topics/rightnow-ai_openfang]]
- [[../topics/othmanadi_planning-with-files]]
- [[../topics/panniantong_agent-reach]]
- [[../topics/jackwener_opencli]]
- [[../topics/duckbugio_flock]]
- [[../topics/omnigent-ai_omnigent]]
- [[../topics/forsy-ai_agent-apprenticeship]]
