---
topic: yeachan-heo_oh-my-claudecode
last_compiled: 2026-07-03
sources:
  - ../../sources/github-Yeachan-Heo_oh-my-claudecode
status: active
---

# oh-my-claudecode

## Summary [coverage: low — 1 source]

Scraped 2026-07-02T02:24:24Z. oh-my-claudecode (OMC) is a teams-first multi-agent orchestration layer built on top of Claude Code, exposing a zero-configuration plugin and CLI that coordinates multiple AI agents across a staged execution pipeline. It extends Claude Code with team orchestration, parallel agent execution, smart model routing, and persistent skill learning — all without requiring users to learn new abstractions beyond natural-language prompts. Available as both a Claude Code marketplace plugin and an npm CLI (`oh-my-claude-sisyphus`), it supports optionally integrating external AI providers such as Codex, Gemini/Antigravity, Grok, and Cursor as tmux-based worker panes. With 37 282 stars by July 2026, it is one of the highest-traction projects in the tracked set.

## Core Pattern [coverage: low — 1 source]

- Team pipeline (canonical): staged execution — `team-plan → team-prd → team-exec → team-verify → team-fix (loop)` — coordinating multiple Claude agents on a shared task list
- tmux CLI workers: `omc team N:<provider>` spawns real provider CLI processes (claude, codex, gemini, antigravity, grok, cursor-agent) as tmux panes; workers die when their task completes
- In-session skills: slash commands (`/team`, `/autopilot`, `/ralph`, `/ultrawork`, `/deep-interview`) drive orchestration inside an active Claude Code session; terminal `omc ...` commands handle CI/headless paths
- Smart model routing: Haiku for simple tasks, Opus for complex reasoning; 19 specialised agent types with a model-compatibility matrix for premium/balanced/budget presets
- Skill learning system: reusable patterns extracted from sessions into YAML skill files (`.omc/skills/` or `~/.omc/skills/`), auto-injected into context when triggers match

## Key Features [coverage: low — 1 source]

- `/team` — canonical in-session multi-agent orchestration with staged pipeline
- `omc team N:<provider>` — tmux CLI workers for Codex, Gemini, Antigravity, Grok, Cursor, Claude
- `/autopilot` — autonomous end-to-end feature execution with minimal ceremony
- `/ralph` — persistent verify/fix loop mode that includes ultrawork parallelism
- `/ultrawork` (`ulw`) — maximum parallelism burst for parallel fixes and refactors
- `/deep-interview` — Socratic requirements clarification via weighted-dimension questioning before any code is written
- `/ccg` — tri-model advisor synthesis routing through `/ask codex` + `/ask antigravity`, synthesised by Claude
- `omc ask <provider>` — run any supported provider CLI and save a markdown artifact
- HUD statusline — real-time orchestration metrics and session observability
- `omc wait` — auto-resume daemon for Claude Code sessions after rate limit resets
- Stop callbacks with Telegram, Discord, and Slack notification tagging
- OpenClaw integration for forwarding session events to external gateway workflows
- Multi-repo workspace support via `.omc-workspace` marker with shared state root

## Tech Stack [coverage: low — 1 source]

- Primary language: TypeScript
- Deployment: Claude Code plugin (marketplace) + npm global CLI (`oh-my-claude-sisyphus`)
- Key dependencies: `better-sqlite3` (native addon for session/skill storage), `@anthropic-ai/claude-agent-sdk` (programmatic session helpers)
- Runtime requirements: Claude Code CLI, Claude Max/Pro subscription or Anthropic API key, tmux (for `omc team` and rate-limit detection)
- Optional providers: Codex CLI, Gemini/Antigravity CLI (`agy`), Grok Build CLI, Cursor agent
- MIT licence

## Traction [coverage: low — 1 source]

- 37 282 stars
- Created 2026-01-09; last pushed 2026-07-01 — actively maintained with frequent releases
- Active Discord community
- Multilingual documentation (English, Korean, Chinese, Japanese, Spanish, Vietnamese, Portuguese)
- Named contributors table with 65+ commit contributors; active sponsorship programme
- GEO visibility benchmark spec included (`geobench/oh-my-claudecode.yaml`)

## Use Cases [coverage: low — 1 source]

- Teams doing coordinated multi-agent software development inside Claude Code without configuration overhead
- End-to-end autonomous feature implementation (`/autopilot`) from vague natural-language requirements
- Tasks requiring guaranteed completion with verify/fix loops (`/ralph`, UltraQA)
- Cross-provider architecture review and design validation (Codex for architecture, Antigravity for UI/UX via `/ccg` or `omc team`)
- CI/CD and headless automation pipelines using deterministic `omc ...` terminal commands
- Projects wanting persistent, reusable skill extraction from solved debugging patterns
- Rate-limited Claude Code workflows needing auto-resume without manual intervention

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — general-purpose multi-agent framework; OMC is Claude-Code-specific and targets developer UX over programmatic graph construction
- [[nousresearch_hermes-agent]] — agentic CLI with tool use; OMC adds team orchestration and provider multiplexing on top of Claude Code rather than being a standalone agent runner
- [[significant-gravitas_autogpt]] — autonomous goal-execution agent; OMC embeds similar persistence loops (`/ralph`) within a Claude Code session rather than as a separate process
- [[gptme_gptme]] — developer-focused terminal agent with multi-agent support; OMC is Claude-Code-native and adds tmux-based multi-provider worker coordination
- [[can1357_oh-my-pi]] — similarly positioned as an orchestration enhancer for an AI coding tool; parallel positioning in the Claude Code ecosystem

## Sources

- [[../../sources/github-Yeachan-Heo_oh-my-claudecode]]
