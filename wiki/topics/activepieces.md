---
topic: activepieces
last_compiled: 2026-06-29
source_count: 1
status: active
---

# Activepieces

## Summary [coverage: high — 1 source]

Activepieces is an open-source, self-hostable AI workflow automation platform positioned as a Zapier replacement and a no-code/low-code automation builder with deep AI and MCP integration. Its core value proposition is a type-safe, extensible "pieces" framework written in TypeScript, where each integration piece is also automatically exposed as an MCP server — making the entire integration library usable directly by LLMs via Claude Desktop, Cursor, or Windsurf. The platform targets both technical and non-technical users, offering a visual flow builder alongside a developer SDK. Dual licensing: MIT for the Community Edition, commercial license for enterprise features. *Source scraped 2026-06-16.*

## Core Pattern [coverage: high — 1 source]

The central abstraction is the **piece** — a TypeScript npm package that encapsulates a third-party integration or capability. Flows are built by composing pieces in a visual builder. At runtime, flows execute as event-triggered pipelines with branching (if/else), looping, auto-retry, and HTTP steps. The AI-first design extends this pattern in two directions:

1. **Agentic flows**: An AI SDK lets builders embed LLM-powered decision steps directly inside flows, enabling agent-style behavior within the workflow graph.
2. **MCP server generation**: Every piece contributed to the platform is simultaneously published as an MCP server. This turns the entire 280+ piece catalog into a tool library that any MCP-compatible LLM client can call, effectively making Activepieces a managed MCP registry.

Human-in-the-loop is a first-class concern: flows can pause for a configurable delay or require explicit human approval before continuing, implemented as pieces built on the same framework.

## Key Features [coverage: high — 1 source]

- **Largest open-source MCP toolkit**: 280+ pieces each available as MCP servers, consumable from Claude Desktop, Cursor, or Windsurf without additional configuration
- **No-code flow builder**: Visual builder with loops, branches, auto-retries, HTTP steps, versioned flows, customizable templates, and multi-language UI
- **Code escape hatch**: "Code" piece supports arbitrary NPM packages in TypeScript; an "ASK AI" mode in the Code piece lets non-technical users write data-cleaning logic by describing it in natural language
- **Native AI pieces**: Built-in integrations for multiple LLM providers for experimentation or production use
- **Human Input Interfaces**: Chat Interface trigger and Form Interface trigger for collecting user input mid-flow
- **Human-in-the-loop controls**: Delay execution or require approval as dedicated pieces
- **Hot reloading for piece development**: Local piece development includes hot reload for rapid iteration
- **Self-hosting with network-gap support**: Full data control; deployable in air-gapped environments
- **Enterprise features**: Custom branding, organizational access controls, developer-set-up / anyone-runs model
- **Open ecosystem**: All piece source code is publicly available and community-contributable; 60% of pieces were contributed by the community; packages published to npmjs.com under `@activepieces`
- **Flow versioning**: Full version history for all flows

## Tech Stack [coverage: high — 1 source]

- **Primary language**: TypeScript (frontend, backend, and all integration pieces)
- **Piece distribution**: npm packages published to npmjs.com (`@activepieces` scope)
- **MCP exposure**: Each piece auto-published as an MCP server
- **Deployment**: Self-hosted (Docker implied by self-hosting docs); also available as a cloud-hosted SaaS at activepieces.com
- **License**: MIT (Community Edition) + Commercial License (enterprise features)
- **Notable integrations covered**: Google Sheets, OpenAI, Discord, RSS, and 200+ additional services

## Traction [coverage: high — 1 source]

- **22,776 GitHub stars** as of the scrape date (2026-06-16)
- **Active development**: `pushed_at` is 2026-06-16, matching the scrape date — indicating ongoing, high-frequency commits
- **Large contributor community**: 60% of the 280+ pieces contributed externally; contributor table in the README lists well over 100 named contributors
- **Discord community**: Active server at discord.gg/2jUXBKDdP8
- **npm ecosystem presence**: All pieces versioned and published to npmjs.com, providing external discoverability
- **Founded 2022**: Repository created 2022-12-03, giving the project roughly 3.5 years of maturation
- **Dual-track adoption**: Community (MIT) + paid enterprise tier signals commercial viability alongside open-source momentum

## Use Cases [coverage: medium — 1 source]

- **Business process automation**: Replacing Zapier/n8n for organizations wanting a self-hosted, data-sovereign workflow platform
- **AI-augmented workflows**: Embedding LLM decision steps into otherwise deterministic automation flows
- **MCP tool hosting**: Serving as the backend that exposes 280+ third-party service integrations as MCP tools consumable by LLM agents
- **Non-technical user automation**: No-code builder enabling business teams to build flows without engineering involvement after initial setup
- **Enterprise workflow governance**: Developer-controlled piece library with org-wide no-code access and approval gates for compliance-sensitive processes
- **Agentic pipelines with human oversight**: Workflows that pause for human approval or input at defined checkpoints

## Related Frameworks [coverage: medium — 1 source]

- **n8n**: The most direct competitor — also an open-source, self-hostable workflow automation platform. Activepieces explicitly positions itself as an n8n alternative (topic tag: `n8n-alternative`) and differentiates primarily on MCP-first design and a fully community-contributable TypeScript piece ecosystem.
- **Zapier / Make (Integromat)**: Cloud-only commercial equivalents. Activepieces targets their user base with a self-hosted, open-source alternative.
- **LangGraph / LangChain**: Pure agent orchestration frameworks with no built-in visual builder or integration catalog. Activepieces approaches agentic behavior from the automation-platform direction rather than the code-first agent framework direction.
- **Dify / Flowise**: Visual LLM workflow builders with agent capabilities. Activepieces overlaps but is broader (full business-process automation) and uniquely MCP-integrated at the piece level.
- **Zapier AI / n8n AI nodes**: Competing approaches to adding AI to automation — Activepieces goes further by making every piece an MCP server, enabling LLM-native consumption rather than just LLM-as-a-step.

## Sources [coverage: high — 1 source]

- [[../../sources/github-activepieces_activepieces]]
