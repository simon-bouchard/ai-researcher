---
topic: activepieces_activepieces
last_compiled: 2026-07-03
sources:
  - ../../sources/github-activepieces_activepieces
status: active
---

# Activepieces

## Summary [coverage: low — 1 source]

Scraped 2026-07-03T23:58:15Z. Activepieces is an open-source AI automation platform and Zapier alternative built around a type-safe TypeScript "pieces" framework. It combines no-code workflow automation with AI agent capabilities, exposing its 280+ integration pieces as MCP servers usable from Claude Desktop, Cursor, and Windsurf. The platform targets both non-technical users via a visual no-code builder and developers who want full customization, enterprise security, and self-hosting.

## Core Pattern [coverage: low — 1 source]

- **Pieces as the core abstraction:** each integration (Google Sheets, OpenAI, Discord, etc.) is a versioned TypeScript npm package — reusable across both workflows and MCP contexts.
- **Visual flow builder:** users compose automation flows using loops, branches, HTTP steps, code steps, and AI steps in a drag-and-drop UI with full version control.
- **MCP-native exposure:** every piece is simultaneously available as an MCP server, meaning any LLM that supports MCP can invoke the same integrations used in visual flows.
- **Human-in-the-loop support:** flows can pause for time delays or explicit human approval before continuing — built on the same piece framework as other integrations.
- **Open ecosystem:** 60% of pieces are community-contributed; all source code is public and pieces are published to npmjs.com upon contribution.

## Key Features [coverage: low — 1 source]

- MCP support: 280+ pieces available as MCP servers for LLM tool use
- No-code visual builder with loops, branches, and auto-retries
- AI-first native pieces for multi-provider LLM experimentation and agent building via an AI SDK
- Human input triggers: chat interface and form interface built in
- Code step with NPM support; ASK AI in code step for non-technical data cleaning
- Hot reloading for local piece development
- Fully versioned flows
- Self-hosted and network-gapped deployment option
- Enterprise features: custom branding, org-level controls (under commercial license)
- Internationalization / language translations (Crowdin-based)
- Customizable flow templates

## Tech Stack [coverage: low — 1 source]

- **Language:** TypeScript
- **Pieces packaging:** npm packages (published to npmjs.com)
- **Deployment:** self-hosted (Docker/local); cloud offering at activepieces.com
- **License:** MIT for Community Edition; commercial license for enterprise features
- **Integration surface:** MCP servers, REST HTTP, custom code (NPM)

## Traction [coverage: low — 1 source]

- **Stars:** 23,102
- **Last push:** 2026-07-03
- **Created:** 2022-12-03
- **Community:** Discord server (discord.gg/2jUXBKDdP8)
- **Contributions:** 60% of pieces contributed by community; large active contributor base
- **Ecosystem:** pieces published to npmjs.com under `@activepieces` scope

## Use Cases [coverage: low — 1 source]

- Replacing Zapier/n8n with a self-hosted, open-source automation platform
- Connecting LLMs to 280+ external services via MCP without custom integration code
- Building AI agents that need to call business tools (sheets, CRMs, messaging platforms)
- Enterprise workflow automation with approval gates and human-in-the-loop steps
- Non-technical users automating data tasks using AI-assisted code steps
- Teams that want developer-built integrations consumable by non-technical colleagues via a no-code UI

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — multi-agent orchestration framework; Activepieces focuses on workflow automation and MCP exposure rather than agent-to-agent conversation patterns
- [[letta-ai_letta]] — persistent memory agent platform; Activepieces is automation-first with MCP integration rather than stateful long-running agents
- [[the-pocket_pocketflow]] — lightweight LLM workflow framework in Python; Activepieces offers a full no-code UI and enterprise deployment where PocketFlow is a minimal code-first library
- [[strands-agents_harness-sdk]] — agent SDK for tool-use orchestration; Activepieces provides a broader no-code automation layer on top of similar MCP/tool concepts

## Sources

- [[../../sources/github-activepieces_activepieces]]
