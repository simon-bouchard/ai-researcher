---
topic: aden-hive_hive
last_compiled: 2026-07-03
sources:
  - ../../sources/github-aden-hive_hive
status: active
---

# Hive (OpenHive)

## Summary [coverage: low — 1 source]

Scraped 2026-07-01T02:48:16Z. Hive (also called OpenHive) is a zero-setup, model-agnostic multi-agent execution harness designed for production AI workloads. It dynamically generates graph-based multi-agent topologies from natural language goal descriptions, eliminating manual orchestration boilerplate. Its key value proposition is providing the production runtime layer — state persistence, crash recovery, cost enforcement, observability, and human-in-the-loop controls — that makes agents reliable enough to run real business processes. Backed by Y Combinator (Aden).

## Core Pattern [coverage: low — 1 source]

- **Goal-to-graph generation:** User defines an objective in plain English; a coding agent automatically compiles a strict, graph-based execution DAG of specialized worker agents.
- **DAG execution with parallel workers:** SDK-wrapped worker nodes execute tasks concurrently within the generated graph, with full observability and tool access.
- **Self-evolving graphs:** On agent failure, the system captures the failure, evolves the execution graph, and redeploys automatically without manual intervention.
- **Persistent role-based memory:** Memory is scoped per agent role and evolves with project context across runs, enabling long-running and stateful workflows.
- **Control plane oversight:** A central control plane monitors real-time metrics, enforces budgets, manages policies, and supports human-in-the-loop intervention nodes with configurable timeouts and escalation.

## Key Features [coverage: low — 1 source]

- Multi-agent coordination for parallel task execution
- Graph-based execution for recurring and complex business processes
- Role-based memory that evolves with project context
- Zero setup — no manual orchestration configuration required
- General compute use and browser use via native extension
- Custom model support (100+ LLM providers via LiteLLM)
- Human-in-the-loop intervention nodes with configurable timeouts
- Granular budget controls: spending limits, throttles, and automatic model degradation per team/agent/workflow
- 102 MCP tools available for agent capabilities
- Session isolation and shared buffers for multi-agent coordination
- Checkpoint-based crash recovery
- Self-hosting supported; also includes a web dashboard (HoneyComb)
- Apache 2.0 open-source license

## Tech Stack [coverage: low — 1 source]

- **Language:** Python (3.11+ required); JavaScript/TypeScript SDK on roadmap
- **LLM integration:** LiteLLM-compatible — supports OpenAI, Anthropic, Google Gemini, DeepSeek, Mistral, Groq, OpenRouter, Ollama, and Hive LLM
- **Tool protocol:** MCP (Model Context Protocol), 102 tools
- **Packaging:** `uv` workspace layout (not pip-installable directly)
- **Deployment:** Self-hosted (quickstart scripts for macOS/Linux and Windows PowerShell); web dashboard at honeycomb.open-hive.com
- **Optional dependency:** ripgrep for faster file search (Python fallback available)

## Traction [coverage: low — 1 source]

- **Stars:** 10,621
- **Last push:** 2026-05-29
- **Created:** 2026-01-12
- Y Combinator-backed company (Aden)
- Active Discord community; Twitter/X at @aden_hq
- Hiring across engineering, research, and go-to-market roles
- Internationalized README (8 languages: English, Chinese, Spanish, Hindi, Portuguese, Japanese, Russian, Korean)

## Use Cases [coverage: low — 1 source]

- Long-running business process automation requiring state persistence and crash recovery
- Production workloads where cost enforcement, observability, and audit trails are required
- Multi-agent pipelines with parallel task execution across CRM, support, messaging, data, and internal APIs
- Workflows requiring human-in-the-loop checkpoints with escalation policies
- Self-healing agent systems that adapt to failures without manual re-engineering
- Teams scaling from agent prototypes to production deployments

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — also targets multi-agent coordination but focuses on conversational agent patterns rather than outcome-driven DAG generation with production harness features
- [[camel-ai_camel]] — multi-agent role-play framework emphasizing agent communication protocols; less focused on production runtime concerns like crash recovery and cost enforcement
- [[significant-gravitas_autogpt]] — early autonomous agent framework with goal decomposition; lacks Hive's graph-evolution and production harness layer
- [[strands-agents_harness-sdk]] — similarly positioned as an agent harness SDK, but lighter-weight and without Hive's self-evolving graph and built-in observability

## Sources

- [[../../sources/github-aden-hive_hive]]
