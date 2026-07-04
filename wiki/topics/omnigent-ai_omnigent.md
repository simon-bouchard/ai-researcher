---
topic: omnigent-ai_omnigent
last_compiled: 2026-07-04
sources:
  - ../../sources/github-omnigent-ai_omnigent
status: active
---

# Omnigent

## Summary [coverage: low — 1 source]

Scraped 2026-07-04T03:03:11Z. Omnigent is an open-source "meta-harness" that provides a common orchestration layer over existing coding-agent CLIs — Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and custom YAML-defined agents — letting users swap or combine harnesses without rewriting workflows, enforce governance policies and sandboxing, and collaborate on agent sessions in real time across terminal, browser, phone, or a native desktop app.

## Core Pattern [coverage: low — 1 source]

- Meta-harness abstraction: a single `omnigent` CLI/server wraps multiple underlying agent harnesses (`claude-sdk`, `claude-native`, `codex`, `codex-native`, `cursor`, `cursor-native`, `hermes`, `hermes-native`, `opencode`, `pi`, `pi-native`, `openai-agents`), selectable per agent YAML
- Session portability: sessions follow the user across terminal, browser, and phone, staying in sync (messages, sub-agents, terminals, files)
- Multi-agent supervision: different harnesses can be mixed in one session, including cross-vendor review (e.g., Claude Code writes, a different-vendor agent reviews)
- Policy engine: function-based policies (approve-before-action, call caps, cost budgets) stack at server, per-agent, and per-session levels, with stricter session-level rules checked first
- Agents defined declaratively in YAML — prompt, tools (local Python functions, MCP servers, or nested sub-agents) — and agents can author new agent YAML files themselves

## Key Features [coverage: low — 1 source]

- Cloud sandbox execution: Modal, Daytona, Islo, E2B, CoreWeave, Kubernetes, OpenShell, Boxlite, or Databricks, launched from the CLI or provisioned per-session server-side ("managed hosts")
- Collaboration primitives: share a live session, co-drive (teammate's messages execute on your machine), and fork (clone a conversation to continue independently)
- Four credential types: first-party API key, Claude/ChatGPT subscription, OpenAI/Anthropic-compatible gateway (OpenRouter, LiteLLM, Ollama, vLLM, Azure), and Databricks workspace profile
- Multi-user server mode (`OMNIGENT_AUTH_ENABLED=1`) with invite-only signup and OIDC SSO (Google, GitHub, Okta, Microsoft)
- Ships example multi-agent setups: Polly (a non-coding tech-lead orchestrator that delegates to Claude Code/Codex/Pi sub-agents in parallel git worktrees and cross-vendor-reviews diffs) and Debby (a two-headed Claude+GPT brainstorming/debate partner)
- Deployment targets: Docker Compose, Render, Railway, Fly.io, Hugging Face Spaces, Modal, Cloudflare (scale-to-zero), Databricks Apps; Cloudflare quick tunnel or Tailscale for reaching a laptop-hosted server without a deploy

## Tech Stack [coverage: low — 1 source]

- Primary language: Python (requires Python 3.12+)
- Distribution: PyPI (`omnigent`), Homebrew tap, or direct git install via `uv tool install`
- Sandboxing: `bwrap` (bubblewrap) on Linux, `seatbelt` on macOS for native harness terminal wrappers; Windows runs in a degraded mode under Job Object process-tree containment (no filesystem/network isolation)
- Requires `tmux` for native harness terminal wrappers; Node.js 22 LTS+ for npm-installed harnesses (Claude, Codex, OpenCode, Pi)
- License: Apache 2.0
- Status: alpha

## Traction [coverage: low — 1 source]

- 6,170 stars
- Created 2026-06-11; pushed 2026-07-04 — very new (about three weeks old) and highly active (pushed same day as scrape)
- Discord community; native macOS desktop app download available; dedicated marketing site (omnigent.ai)

## Use Cases [coverage: low — 1 source]

- Teams standardizing on one orchestration/governance layer while letting individual developers pick their preferred underlying coding agent
- Remote/mobile agent supervision — starting a session on a laptop and continuing from a phone
- Organizations needing spend caps, tool-access limits, or approval gates across multiple agent harnesses uniformly
- Cross-vendor code review workflows (one vendor's agent writes, another's reviews) for reduced correlated blind spots
- Teaching/pairing scenarios via session co-driving and live sharing

## Related Frameworks [coverage: low — 1 source]

- [[gitlawb_openclaude]] — OpenClaude is a single-CLI, multi-provider fork of Claude Code itself; Omnigent instead orchestrates multiple *separate* harnesses (including OpenClaude-like CLIs) from one meta-layer
- [[duckbugio_flock]] — Flock is a narrow chat-triggered dev-team pipeline built only on Claude Code; Omnigent is a general-purpose meta-harness spanning many harnesses and transports
- [[opensandbox-group_opensandbox]] and [[e2b-dev_e2b]] — both are sandbox providers Omnigent can launch cloud sessions into, rather than competitors
- [[strands-agents_harness-sdk]] — a single-harness SDK, whereas Omnigent sits a layer above, orchestrating across harnesses like this one
- [[forsy-ai_agent-apprenticeship]] — also wraps multiple existing coding-agent CLIs, but focuses on extracting reusable learning signal from runs rather than live orchestration/governance

## Sources

- [[../../sources/github-omnigent-ai_omnigent]]
