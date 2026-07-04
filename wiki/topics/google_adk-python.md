---
topic: google_adk-python
last_compiled: 2026-07-03
sources:
  - ../../sources/github-google_adk-python
status: active
---

# Agent Development Kit (ADK)

## Summary [coverage: low — 1 source]

Scraped 2026-07-03T23:58:26Z. Google's Agent Development Kit (ADK) is an open-source, code-first Python framework for building, evaluating, and deploying sophisticated AI agents, released in version 2.0 with breaking API changes. ADK 2.0 introduces a graph-based Workflow runtime and a structured Task API for agent-to-agent delegation, positioning it as a production-grade toolkit for composing deterministic multi-agent pipelines. It is primarily designed for use with Gemini models and targets Google Cloud deployment, though the core API is model-agnostic.

## Core Pattern [coverage: low — 1 source]

- Two primary abstractions: `Agent` (instructions, tools, behavior) and `Workflow` (graph-based orchestration of agents and tasks)
- Graph-based Workflow runtime: routing, fan-out/fan-in, loops, retry, state management, dynamic nodes, human-in-the-loop, nested workflows
- Task API: structured agent-to-agent delegation with multi-turn task mode, single-turn controlled output, mixed delegation patterns
- Task agents usable as nodes within Workflow graphs
- `adk run` (CLI) and `adk web` (browser UI) for local development and testing

## Key Features [coverage: low — 1 source]

- Graph-based deterministic execution engine for agentic workflows
- Human-in-the-loop support at both Task and Workflow levels
- Optional extensions via `google-adk[extensions]`
- Built-in web UI for multi-agent directory inspection (`adk web`)
- Session compatibility: ADK 2.0 sessions readable by ADK 1.28+
- Bi-weekly release cadence
- Apache 2.0 license; published by Google

## Tech Stack [coverage: low — 1 source]

- Language: Python 3.10+
- Package: `google-adk` on PyPI
- Default model: Gemini 2.5 Flash (referenced in Quick Start)
- Deployment: designed for Google Cloud / Vertex AI integration
- Companion repos: `google/adk-samples` (samples), `google/adk-web` (web UI)

## Traction [coverage: low — 1 source]

- 20,435 stars
- Created 2025-04-01; pushed 2026-07-03 — very active, over 15 months of development at scrape time
- Backed by Google; topics span `multi-agent-systems`, `agents-sdk`, `genai`, `agentic-ai`
- Bi-weekly release cadence signals sustained investment

## Use Cases [coverage: low — 1 source]

- Building production multi-agent pipelines with deterministic, graph-based orchestration
- Structured agent-to-agent delegation where task outputs need controlled format
- Applications requiring human approval steps embedded in automated workflows
- Gemini-first agentic applications targeting Google Cloud infrastructure
- Teams that want a code-first approach with explicit graph definition rather than LLM-driven orchestration

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — Microsoft's multi-agent framework; ADK is Google's counterpart with stronger graph/workflow primitives in v2.0
- [[microsoft_agent-framework]] — another large-vendor agent SDK; ADK distinguishes itself with the Workflow graph execution engine
- [[langroid_langroid]] — research-origin multi-agent framework; ADK is more opinionated about deployment to cloud infrastructure
- [[pydantic_pydantic-ai]] — lightweight agent SDK with Pydantic-first design; ADK is heavier but offers built-in workflow orchestration
- [[strands-agents_harness-sdk]] — AWS-backed agent harness; ADK is the Google-backed equivalent

## Sources

- [[../../sources/github-google_adk-python]]
