---
topic: harness-sdk
last_compiled: 2026-06-29
source_count: 1
status: active
---

# Strands Agents (harness-sdk)

## Summary [coverage: high — 1 source]

Strands Agents is an open-source SDK for building and running production AI agents in Python and TypeScript. Its stated value proposition is a "model-driven approach" that lets developers construct an agent harness and control it end-to-end — from simple conversational assistants to complex autonomous workflows — with minimal boilerplate. The SDK ships with built-in context management, execution limits, observability hooks, guardrails, and multi-agent support out of the box, positioning itself as a complete production toolkit rather than a minimal orchestration layer.

*Source scraped: 2026-06-16T03:10:35Z.*

---

## Core Pattern [coverage: high — 1 source]

The central abstraction is the **Agent loop** — a traced execution cycle that records every model decision by default. Developers instantiate an `Agent`, attach tools, and invoke it with a prompt; the loop handles tool-calling, result injection, and iteration until the task completes or a limit is reached.

Key abstractions:

- **Agent loop** — the core execution engine, fully observable via built-in tracing
- **Hooks** — intercept any step in the loop to log, validate, or redirect execution
- **Guardrails** — pre-execution checks that catch mistakes before a tool call runs
- **Steering handlers** — allow the agent to self-correct rather than fail silently
- **Multi-agent patterns** — supported natively in both Python and TypeScript SDKs
- **Structured output** — built-in; TypeScript variant uses Zod-typed tool schemas
- **Bidirectional streaming** — supported in the Python SDK

The design philosophy emphasizes staying in control: every decision is traceable, backends are swappable without code changes, and the agent harness is explicit rather than implicit.

---

## Key Features [coverage: high — 1 source]

- **MCP (Model Context Protocol) support** — built in; a companion `strands-agents/mcp-server` repository is also maintained
- **Model agnosticism** — first-class provider support for Amazon Bedrock (default), Anthropic, OpenAI, Gemini, and Ollama; custom providers also supported via a provider interface
- **Dual-language SDKs** — Python (`strands-agents` on PyPI, requires Python 3.10+) and TypeScript (`@strands-agents/sdk` on npm, requires Node.js 20+) with feature parity
- **WebAssembly bridge** — `strands-wasm` package enables Python tools to run from TypeScript agents via WASM bindings (WIT interface)
- **Observability by default** — agent loop traces every decision without additional configuration
- **Execution hooks** — intercept and modify any loop step (logging, validation, redirection)
- **Guardrails** — pre-run validation layer to prevent erroneous tool calls
- **Streaming** — bidirectional streaming in Python SDK
- **Developer CLI** (`strandly`) — local builds, codegen, and workspace tooling
- **Agent Builder** — companion repository for a higher-level agent construction UI
- **Apache 2.0 license** — open-source, permissive

---

## Tech Stack [coverage: high — 1 source]

- **Primary language:** Python (SDK); TypeScript (SDK); WebAssembly (interop bridge)
- **Python requirements:** Python 3.10+; packaged via Hatch; distributed on PyPI as `strands-agents` + `strands-agents-tools`
- **TypeScript requirements:** Node.js 20+; distributed on npm as `@strands-agents/sdk`
- **Default model provider:** Amazon Bedrock (Claude Sonnet); other providers configurable
- **Monorepo structure:** single repo containing Python SDK, TypeScript SDK, WASM bindings, developer CLI, and documentation site (Astro/Starlight)
- **Notable dependencies/integrations:** Amazon Bedrock, Anthropic API, OpenAI API, Google Gemini, Ollama, MCP protocol
- **Deployment model:** cloud-agnostic; any cloud or local; production deployment guide provided

---

## Traction [coverage: medium — 1 source]

- **Stars:** 6,161 as of scrape date (2026-06-16)
- **Repository created:** 2025-05-14 — approximately 13 months old at scrape time
- **Last pushed:** 2026-06-16 — actively maintained, pushed the same day as scrape
- **Community:** Discord server at discord.gg/strands
- **GitHub topics:** 20 topics including `agent-framework`, `multi-agent-systems`, `llm-agent`, `mcp`, `anthropic`, `bedrock`, `openai` — broad discoverability signal
- **Ecosystem:** companion repositories for tools (`strands-agents/tools`), samples (`strands-agents/samples`), MCP server (`strands-agents/mcp-server`), and Agent Builder (`strands-agents/agent-builder`) suggest an organized, multi-repo ecosystem
- **Packages:** published on both PyPI and npm, indicating dual-ecosystem commitment
- **Activity signal:** active commit history badge shown in README; open issues and PRs badges present

---

## Use Cases [coverage: medium — 1 source]

- **Production AI agents** — explicitly positioned for production deployment; ships with observability, guardrails, and a deployment guide
- **Autonomous workflows** — multi-step agentic tasks with tool-calling, looping, and self-correction
- **Multi-agent systems** — native multi-agent patterns for orchestrating fleets of specialized agents
- **Cloud-native deployment** — any cloud backend via swappable model providers; particularly aligned with AWS/Bedrock environments given the default provider
- **Conversational assistants** — simple single-turn or multi-turn agents at the low-complexity end
- **Cross-language teams** — Python and TypeScript parity allows backend and frontend/Node teams to share agent primitives
- **MCP-integrated pipelines** — tool ecosystems built on the Model Context Protocol

---

## Related Frameworks [coverage: low — 1 source]

Based on the source file's topics and stated scope:

- **LangGraph** — also targets production, complex agentic workflows; LangGraph emphasizes graph-based state machines whereas Strands centers on a hook-interceptable loop
- **LlamaIndex Workflows** — similar event-loop model; LlamaIndex has deeper RAG/retrieval integration out of the box
- **AutoGen (Microsoft)** — also multi-agent native; AutoGen is more research-oriented; Strands explicitly targets production
- **Pydantic AI** — Python-first, typed agent framework; narrower scope (Python only, no WASM bridge)
- **OpenAI Agents SDK** — model-specific (OpenAI); Strands is model-agnostic with OpenAI as one of several providers
- **CrewAI** — role-based multi-agent orchestration; Strands is more general-purpose with lower-level control primitives

Strands differentiates primarily through: model/cloud agnosticism, dual Python+TypeScript SDKs with WASM interop, built-in production observability and guardrails without third-party add-ons, and the hook-interceptable agent loop design.

---

## Sources [coverage: high — 1 source]

- [[../../sources/github-strands-agents_harness-sdk]]
