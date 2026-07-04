---
topic: duckbugio_flock
last_compiled: 2026-07-04
sources:
  - ../../sources/github-duckbugio_flock
status: active
---

# Flock

## Summary [coverage: low — 1 source]

Scraped 2026-07-04T03:03:13Z. Flock runs a Claude Code-powered AI dev team on a self-hosted server, driven entirely from chat (Telegram or VK). Users describe a feature in a chat message; a pipeline of native Claude Code subagents (planner → coder → tester → reviewer → arbiter) plans it, builds it on a branch, tests it, reviews it, and opens a PR — with each chat isolated in its own sandboxed workspace.

## Core Pattern [coverage: low — 1 source]

- Five-subagent pipeline — planner, coder, tester, reviewer, arbiter — implemented as native Claude Code subagents (`core/agents/`); a plain question is answered directly, a build request triggers the full team
- Arbiter acts as a risk-aware, cycle-limited loop-breaker so reviewer/coder cycles never spin forever; escalates to the human user when needed instead of looping indefinitely
- Chat-as-task-source: the conversation itself is the spec; the bot's shell and editor are sandboxed inside the container
- Poll-based PR-review integration — the bot polls the git host for new review comments rather than requiring inbound webhooks, so it works even when the host can't reach the bot
- Per-chat workspace isolation (`/workspace/chat_<id>`), with parallel execution capped by `MAX_CONCURRENT_CHAT_RUNS`

## Key Features [coverage: low — 1 source]

- Multi-transport core: Telegram and VK today on a shared platform-agnostic core (`core/`), with each platform a thin adapter (`adapters/<name>/`)
- Built for microservices workspaces: a single feature can span several repos, coordinating one branch and one cross-linked PR per repo
- Runs on a Claude Pro/Max subscription (no per-token billing) or an Anthropic API key
- Git host support: Gitea, GitHub, and GitLab, with `gh` CLI integration for github.com
- Voice message support (transcription via Mistral, OpenAI, or local provider) run as commands
- Optional dind sidecar for dockerized linters/tests inside the agent's sandbox
- Ansible-based one-command VPS deploy (Telegram) with inbound-webhook + Caddy TLS proxy as an alternative to polling

## Tech Stack [coverage: low — 1 source]

- Primary language: Go 1.26
- Distribution: prebuilt Docker images (`ghcr.io/duckbugio/flock-telegram`, `ghcr.io/duckbugio/flock-vk`) — no build step required
- CI/build runner: Task (taskfile.dev) — `task lint`, `task tests`, `task build`
- Monorepo layout: platform-agnostic core plus per-platform adapters
- License: MIT

## Traction [coverage: low — 1 source]

- 573 stars
- Created 2026-06-08; pushed 2026-07-02 — very new (under a month old) and actively developed
- Region constraint: requires hosting in an Anthropic-supported region (e.g., not RU/CN)

## Use Cases [coverage: low — 1 source]

- Small teams or solo developers who want a persistent, chat-driven AI dev team instead of an interactive terminal coding agent
- Organizations already using Telegram or VK as internal communication tools who want to trigger builds/PRs from chat
- Multi-repo/microservices projects needing coordinated cross-repo PRs from a single feature request
- Self-hosted deployments where Claude subscription billing (rather than per-token API cost) is preferred

## Related Frameworks [coverage: low — 1 source]

- [[nousresearch_hermes-agent]] — another chat-oriented agent runtime; Flock is narrowly focused on a chat-triggered dev-team pipeline built specifically on Claude Code subagents
- [[gitlawb_openclaude]] — both extend Claude Code-style coding-agent workflows, but OpenClaude is a multi-provider CLI fork while Flock is a chat-driven, sandboxed dev-team orchestrator
- [[omnigent-ai_omnigent]] — broader meta-harness orchestrating many coding agents across many transports; Flock is a narrower, single-purpose chat-to-PR pipeline built only on Claude Code
- [[opensandbox-group_opensandbox]] — shares the theme of sandboxed per-session isolation for agent execution

## Sources

- [[../../sources/github-duckbugio_flock]]
