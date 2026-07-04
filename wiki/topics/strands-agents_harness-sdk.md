---
topic: strands-agents_harness-sdk
last_compiled: 2026-07-03
sources:
  - ../../sources/github-strands-agents_harness-sdk
status: active
---

# Strands Agents

## Summary [coverage: low — 1 source]

Scraped 2026-06-16T03:10:35Z. Strands Agents is an open-source SDK for building and running AI agents using a model-driven approach, available in both Python and TypeScript. It targets production deployments and offers built-in context management, observability, guardrails, and an interceptable agent loop. The SDK is model-agnostic with first-class support for Amazon Bedrock, Anthropic, OpenAI, and Gemini, and emphasizes developer control end-to-end. Released in May 2025, it reached 6 161 stars by June 2026 with an active release cadence.

## Core Pattern [coverage: low — 1 source]

- Model-driven agent loop: agents are defined by model + tools; the loop traces every decision by default and can be intercepted via hooks at any step
- Hooks and steering: hooks allow logging, validation, or redirection at any point in execution; steering handlers let agents self-correct instead of failing silently
- Guardrails: catch mistakes before tool calls execute, preventing silent failures in production
- Multi-SDK monorepo: Python SDK (`strands-py/`) and TypeScript SDK (`strands-ts/`) share the same abstractions; WebAssembly bindings (`strands-wasm/`) allow Python tools to run from TypeScript agents
- MCP and multi-agent built-in: MCP, streaming, multi-agent patterns, and structured output are included without additional configuration

## Key Features [coverage: low — 1 source]

- Model-agnostic: supports Amazon Bedrock, Anthropic, OpenAI, Gemini, Ollama, and custom providers; swap backends without changing agent code
- Agent loop with full traceability: every decision is traced by default
- Hook system for intercepting any step (logging, validation, redirect)
- Guardrails to catch and block erroneous actions before execution
- Steering handlers for in-loop agent self-correction
- Built-in MCP support, bidirectional streaming, and structured output
- Python SDK: `pip install strands-agents strands-agents-tools`, requires Python 3.10+
- TypeScript SDK: `npm install @strands-agents/sdk`, requires Node.js 20+
- WebAssembly bindings enabling Python tools to be used from TypeScript agents
- Developer CLI (`strandly/`) for local builds, codegen, and workspace tooling
- Apache 2.0 licensed; community on Discord

## Tech Stack [coverage: low — 1 source]

- Primary languages: Python (3.10+), TypeScript (Node.js 20+)
- Build tooling: Hatch (Python), npm (TypeScript), Astro/Starlight (docs site)
- Default model provider: Amazon Bedrock (Claude Sonnet); configurable to Anthropic, OpenAI, Gemini, Ollama, and others
- Key integrations: MCP, WebAssembly (cross-language tool sharing)
- Deployment: any cloud; production deployment guide available

## Traction [coverage: low — 1 source]

- 6 161 stars
- Created 2025-05-14; last pushed 2026-06-16 — active development, roughly one year old
- Monthly commit activity tracked via GitHub badge
- Community Discord at discord.gg/strands
- Published on PyPI (`strands-agents`) and npm (`@strands-agents/sdk`)

## Use Cases [coverage: low — 1 source]

- Building production AI agents requiring observability and guardrails from day one
- Teams that need model/cloud portability without rewriting agent code
- Multi-agent workflows requiring built-in coordination patterns
- Agents needing MCP tool integration or structured output
- Cross-language agent development (Python logic accessible from TypeScript via WASM)
- Conversational assistants through to complex autonomous workflows at scale

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — multi-agent orchestration framework from Microsoft; conversation-centric design vs. Strands's model-driven loop-with-hooks approach
- [[google_adk-python]] — Google's Agent Development Kit; similar production focus but tied to the Google Cloud/Gemini ecosystem
- [[pydantic_pydantic-ai]] — Python-first agent framework with strong type safety via Pydantic; less emphasis on cross-language or WebAssembly support
- [[letta-ai_letta]] — focuses on persistent agent memory and stateful agents; Strands focuses on control and observability of the execution loop
- [[zhayujie_cowagent]] — also self-describes as an "Agent Harness" but is a complete self-hostable assistant platform with channels and memory, not a developer SDK

## Sources

- [[../../sources/github-strands-agents_harness-sdk]]
