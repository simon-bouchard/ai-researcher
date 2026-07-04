---
topic: the-pocket_pocketflow
last_compiled: 2026-07-03
sources:
  - ../../sources/github-The-Pocket_PocketFlow
status: active
---

# PocketFlow

## Summary [coverage: low — 1 source]

Scraped 2026-06-16T03:10:31Z. PocketFlow is a minimalist LLM framework implemented in just 100 lines of Python with zero external dependencies and zero vendor lock-in. It exposes a single core abstraction — a directed graph — from which agents, multi-agent systems, workflows, RAG pipelines, and other common patterns can all be composed. The project emphasizes "Agentic Coding," a development paradigm where human designers write specs and AI coding agents (e.g., Cursor) implement the flow code. With 10 762 stars and ports in TypeScript, Java, C++, Go, Rust, and PHP, it has attracted strong cross-language adoption since its December 2024 launch.

## Core Pattern [coverage: low — 1 source]

- Graph as the sole abstraction: the entire framework is a directed graph of nodes with typed action-based edges; all higher-level patterns are built on top of this
- Node-action-edge routing: each node executes a step and returns an action string; edges map actions to successor nodes, enabling conditional branching and loops without special primitives
- Composable flows: a Flow is itself a Node, enabling nested and hierarchical compositions (e.g., a patch step implemented as a subflow inside a larger coding agent flow)
- No built-in wrappers: no app-specific or vendor-specific wrappers included; integrations with LLM providers, vector stores, or tools are left entirely to the user
- Agentic Coding workflow: intended usage is human-authored design docs fed to an AI coding agent that generates flow code, keeping the framework surface area minimal enough for reliable AI generation

## Key Features [coverage: low — 1 source]

- 100-line core (~56 KB installed), no third-party dependencies
- Supports agents, multi-agent systems, workflows, RAG, batch processing, parallel execution, streaming, map-reduce, human-in-the-loop, and chain-of-thought patterns
- MCP (Model Context Protocol) integration supported via cookbook example
- A2A (Agent-to-Agent) protocol support for inter-agent communication
- Real-time streaming with user interrupt capability
- Supervisor / self-healing patterns (error recovery loops)
- Extensive cookbook: 40+ tutorials ranging from beginner to advanced
- Multi-language ports: TypeScript, Java, C++, Go, Rust, PHP
- Available via `pip install pocketflow` or by copying the 100-line source directly

## Tech Stack [coverage: low — 1 source]

- Primary language: Python; official ports in TypeScript, Java, C++, Go, Rust, PHP
- Dependencies: none (zero external dependencies in core)
- Deployment: library — import and compose; no server or daemon required
- Installation: `pip install pocketflow` or copy source
- MIT licence

## Traction [coverage: low — 1 source]

- 10 762 stars
- Created 2024-12-24; last pushed 2026-03-27 — active during first year, somewhat slower recently
- Active Discord community
- README translated into 8 languages (Chinese, Spanish, Japanese, German, Russian, Portuguese, French, Korean)
- 40+ cookbook tutorials; multiple full application tutorials with separate design doc and flow code repos
- Multiple language ports indicate strong community engagement

## Use Cases [coverage: low — 1 source]

- Building LLM-powered agents and multi-agent systems with minimal framework overhead
- RAG pipelines and agentic RAG where the agent decides which documents to retrieve
- Batch and parallel processing workflows (translation, resume qualification, image processing)
- Production coding agents with tools, memory, and self-healing subflows
- Document-to-podcast, newsletter curation, invoice extraction, and lead generation pipelines
- Real-time chat interfaces via FastAPI WebSocket or Streamlit with human-in-the-loop state machines
- Prototyping via "Agentic Coding" — human writes design doc, AI agent generates flow code

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — also supports multi-agent and async patterns but ships many built-in abstractions and vendor integrations; PocketFlow trades breadth for a 100-line footprint
- [[langroid_langroid]] — task-based multi-agent framework with richer built-in tooling; PocketFlow stays at the graph primitive level with no app-specific wrappers
- [[camel-ai_camel]] — role-playing multi-agent framework with structured agent communication protocols; PocketFlow is more general-purpose and lower-level
- [[google_adk-python]] — Google's agent framework with deeper tool and service integration; PocketFlow is vendor-agnostic and dependency-free
- [[hkuds_nanobot]] — another minimalist agent approach; PocketFlow is a composable graph framework where NanoBot targets end-user personal assistant tasks

## Sources

- [[../../sources/github-The-Pocket_PocketFlow]]
