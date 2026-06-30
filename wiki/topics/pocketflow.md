---
topic: pocketflow
last_compiled: 2026-06-29
source_count: 1
status: active
---

# PocketFlow

## Summary [coverage: high — 1 source]

PocketFlow is a minimalist Python LLM framework whose entire core is 100 lines of code. Its value proposition is the inverse of frameworks like LangChain or CrewAI: instead of shipping hundreds of thousands of lines, app-specific wrappers, and vendor integrations, PocketFlow ships a single primitive — a graph abstraction — and leaves everything else to the developer. Installation is `pip install pocketflow` or literally copying the 100-line source file. Zero external dependencies, zero vendor lock-in, package size of ~56 KB.

The project was created on 2024-12-24, last pushed 2026-03-27, and was scraped on 2026-06-16.

## Core Pattern [coverage: high — 1 source]

The fundamental abstraction is a **directed graph**: nodes perform LLM calls or tool operations, edges carry conditional routing between them. From this single primitive the framework supports all mainstream agentic design patterns without adding framework-level scaffolding for each one:

- **Agent / ReAct loop** — a node iterates with tool-calling until a termination condition routes to an exit edge
- **Multi-Agent** — multiple graph flows communicate asynchronously; a supervisor flow can wrap an agent sub-flow for reliability
- **Workflow** — linear or branching sequences of nodes (write → outline → style, etc.)
- **RAG / Agentic RAG** — retrieval is a node in the graph; the agentic variant adds a routing decision for which documents to fetch
- **Map-Reduce** — parallel fan-out nodes with a reduce aggregation node
- **Batch** — a batch-aware node type processes items in parallel; cookbook shows 8x speedup on image processing
- **Finite State Machine** — graph edges encode state transitions; used in Streamlit UI examples with human-in-the-loop checkpoints
- **Memory** — short-term (in-node conversation history) and long-term (external storage node) patterns both implemented as graph sub-flows

The design philosophy is called **Agentic Coding**: humans author a design document, then delegate code generation to an AI coding assistant (e.g. Cursor). PocketFlow's minimal surface area makes it tractable for an LLM to read and reason about the full framework before generating application code.

## Key Features [coverage: high — 1 source]

- **MCP (Model Context Protocol) support** — cookbook example shows an agent node using MCP for tool dispatch
- **A2A (Agent-to-Agent) protocol** — wraps a PocketFlow agent with A2A for inter-agent communication across systems
- **RAG and Agentic RAG** — both simple retrieval pipelines and agent-driven document selection
- **Streaming** — real-time LLM token streaming with user interrupt capability
- **Human-in-the-loop (HITL)** — CLI and Streamlit FSM variants; pause-and-resume via graph edges
- **Voice pipeline** — VAD + STT + LLM + TTS wired as graph nodes
- **LLM-as-Judge loop** — evaluator-optimizer pattern as a graph cycle
- **Self-healing flows** — error recovery via conditional routing edges (e.g. Mermaid diagram generator with auto-correction)
- **Heartbeat / periodic monitoring** — nested flows for always-on agents
- **FastAPI integration** — WebSocket streaming and SSE background job patterns in cookbook
- **Streamlit integration** — UI state machine examples
- **Multi-language ports** — TypeScript, Java, C++, Go, Rust, and PHP implementations maintained under The-Pocket org
- **Batch translation** — README translated into Chinese, Spanish, Japanese, German, Russian, Portuguese, French, Korean (also used as a cookbook example of the batch pattern)

## Tech Stack [coverage: medium — 1 source]

- **Primary language:** Python (core library)
- **Additional language ports:** TypeScript, Java, C++, Go, Rust, PHP (separate repos under The-Pocket organization)
- **Dependencies:** none (the 100-line core has zero imports beyond the standard library; LLM client libraries are user-supplied)
- **Deployment model:** library — `pip install pocketflow`; alternatively copy the single source file directly into a project
- **LLM provider:** user-configured; the framework is provider-agnostic by design (no vendor wrappers bundled)
- **UI integration examples:** Streamlit, FastAPI (WebSocket + SSE)
- **Packaging size:** ~56 KB (compare: LangChain +166 MB, CrewAI +173 MB, LangGraph +51 MB)

## Traction [coverage: high — 1 source]

- **10,762 GitHub stars** as of scrape date (2026-06-16) — notable for a framework created in December 2024, indicating rapid growth within roughly 18 months
- Active Discord community (invite link in README)
- Active cookbook with 30+ examples spanning beginner through advanced difficulty
- External tutorial app repositories maintained by the author (Website Chatbot, Codebase Knowledge Builder, YouTube Summarizer, Cold Opener Generator, etc.) demonstrating real-world application patterns
- Video tutorials on YouTube channel (ZacharyLLM)
- Substack blog documenting the "Agentic Coding" methodology
- Multi-language ports (TypeScript, Java, C++, Go, Rust, PHP) indicate active community contribution or author investment in cross-platform reach
- README translated into 8 languages, suggesting global adoption interest

## Use Cases [coverage: high — 1 source]

PocketFlow is best suited for:

- **Agentic coding projects** where a developer (or AI assistant) needs to read and understand the full framework before generating application code — the 100-line core makes this tractable
- **Prototyping and experimentation** — minimal setup, no dependency conflicts, copy-paste deployment
- **Educational use** — the large cookbook (30+ examples, tiered by difficulty) and tutorial app repos make it a strong teaching tool for LLM application patterns
- **Production workflows** with FastAPI or Streamlit frontends — multiple cookbook examples cover deployment-ready patterns
- **Multi-agent systems** requiring A2A or MCP integration
- **Batch and parallel processing** pipelines (document translation, resume qualification, map-reduce research)
- **Automation pipelines** — lead generation, newsletter curation, invoice processing, periodic monitoring
- **Voice and multimodal applications** — voice chat pipeline, PDF invoice extraction with vision

Less suited for teams that need pre-built vendor integrations, managed memory stores, or out-of-the-box observability tooling — those must be wired in by the developer.

## Related Frameworks [coverage: medium — 1 source]

The README provides a direct comparison table:

| Framework | Lines | Package size | App-specific wrappers | Vendor wrappers |
|---|---|---|---|---|
| LangChain | 405K | +166 MB | Many | Many |
| CrewAI | 18K | +173 MB | Many | Many |
| SmolAgent | 8K | +198 MB | Some | Some |
| LangGraph | 37K | +51 MB | Some | Some |
| AutoGen | 7K (core) | +26 MB (core) | Some | Many (optional) |
| **PocketFlow** | **100** | **+56 KB** | **None** | **None** |

- **LangGraph** is the closest architectural relative — both use a graph abstraction — but LangGraph ships with Postgres/SQLite persistence backends, semantic search integrations, and a 37K-line surface area. PocketFlow deliberately omits all of that.
- **LangChain** and **CrewAI** are the maximal-wrapper alternatives; PocketFlow positions itself as the antithesis of that approach.
- **AutoGen** and **SmolAgent** are agent-centric without a graph primitive; PocketFlow's graph covers agent loops as a special case.
- The Typescript port overlaps with frameworks like **LangChain.js** and **Mastra** in the JS/TS ecosystem.

## Sources [coverage: high — 1 source]

- [[../../sources/github-The-Pocket_PocketFlow]]
