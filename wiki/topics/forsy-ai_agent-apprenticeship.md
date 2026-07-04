---
topic: forsy-ai_agent-apprenticeship
last_compiled: 2026-07-04
sources:
  - ../../sources/github-Forsy-AI_agent-apprenticeship
status: active
---

# Agent Apprenticeship

## Summary [coverage: low — 1 source]

Scraped 2026-07-04T03:03:15Z. Agent Apprenticeship is an open ecosystem where AI agents complete real-world tasks through iterative workflow loops, are evaluated by mentor agents or humans, and turn completed work into reusable "experience compilations" — structured training/learning signals — that improve future agent runs. It ships as a CLI (`apprentice` / `agent-apprenticeship`) that wraps existing coding agents (Claude Code, Codex, Cursor, OpenClaw, OpenCode, Hermes Agent, or custom agents) rather than replacing them.

## Core Pattern [coverage: low — 1 source]

- Apprentice/mentor loop: an "Apprentice Agent" (a wrapped local coding agent) executes a task while a "Mentor Model Provider" evaluates and guides iterative execution
- Three Apprenticeship Modes: Autonomous, Expert-Led, and Organization Custom — controlling how much human-in-the-loop oversight is applied
- Output of every run is an "Experience Compilation" — a structured record of the task, execution trace, and learning signal, which can be installed as "Runtime Training" for future runs
- Ecosystem exchange model: users can search, inspect, pull, and export Experience Compilations from a shared Public Ecosystem, or keep them Private Internal Only
- Configurable loop depth (`AA_MAX_ITERATIONS`) to bound iterative execution

## Key Features [coverage: low — 1 source]

- Agent-agnostic wrapper: auto-detects installed CLIs (Codex, Cursor, Claude Code, OpenClaw, OpenCode, Hermes Agent) or accepts a custom command template
- Seed dataset (v0.2, published on Hugging Face) with 500+ curated real-world tasks, 495 reusable agent lessons, 1000+ execution traces, 1000+ work episodes, and 505 full experience compilations
- `apprentice ecosystem search/inspect/pull` for browsing and reusing community-contributed experience
- `apprentice learn install` to install prior Runtime Training into a new run
- `apprentice doctor` / `apprentice settings` for setup diagnostics and configuration
- Mentor model provider support: OpenAI, Anthropic, Gemini, OpenRouter (via local `.env.local` keys)

## Tech Stack [coverage: low — 1 source]

- Primary distribution: npm package (`agent-apprenticeship`, installed globally or via `npx`)
- Primary language of the underlying implementation: Python (per repo metadata), with an npm-distributed CLI wrapper
- Local config/keys stored in `~/.agent-apprenticeship/.env.local`
- Repo layout: `bin/`, `src/`, `schemas/`, `examples/`, `selected_ale_tasks_demo/`

## Traction [coverage: low — 1 source]

- 1,193 stars
- Created 2026-06-19; pushed 2026-07-03 — very new (about two weeks old) and actively developed
- Published companion dataset on Hugging Face (`Forsy-AI/agent-apprenticeship-seed-dataset_v0.2`)

## Use Cases [coverage: low — 1 source]

- Teams wanting to convert routine agent task execution into reusable training signal for future runs
- Organizations comparing agent performance across CLIs (Codex vs. Claude Code vs. Cursor, etc.) on the same task set
- Building a shared, cross-organization corpus of real-world agent task traces for post-training or evaluation
- Researchers studying agent learning/self-improvement via execution traces rather than raw model fine-tuning

## Related Frameworks [coverage: low — 1 source]

- [[omnigent-ai_omnigent]] — both wrap multiple existing coding-agent CLIs, but Omnigent focuses on live orchestration/collaboration while Agent Apprenticeship focuses on post-hoc learning signal extraction
- [[nousresearch_hermes-agent]] — one of the supported Apprentice Agents; Agent Apprenticeship treats it as a pluggable backend rather than extending it directly
- [[gitlawb_openclaude]] — comparable in wrapping Claude Code-style workflows, but Agent Apprenticeship is data/learning-focused rather than a CLI replacement

## Sources

- [[../../sources/github-Forsy-AI_agent-apprenticeship]]
