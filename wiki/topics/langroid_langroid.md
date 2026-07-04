---
topic: langroid_langroid
last_compiled: 2026-07-03
sources:
  - ../../sources/github-langroid_langroid
status: active
---

# Langroid

## Summary [coverage: low — 1 source]

Scraped 2026-06-16T03:10:41Z. Langroid is a lightweight, extensible Python framework for building LLM-powered multi-agent applications, developed by researchers at CMU and UW-Madison. Its core abstraction is the Actor-model-inspired Agent+Task pair: agents encapsulate LLM conversation state, an optional vector store, and tools; tasks wrap agents with orchestration logic and enable hierarchical, recursive multi-agent collaboration via message passing. Langroid avoids LangChain and other frameworks entirely, supports practically any LLM provider, and prioritizes developer experience with Pydantic-based tool definitions that eliminate manual JSON schema writing. Production usage is cited from Nullify (secure software development), and a multi-agent RAG system for pharmacovigilance was published in ML for Healthcare 2024.

## Core Pattern [coverage: low — 1 source]

- Agent+Task abstraction: `ChatAgent` manages LLM conversation state; `Task` wraps an agent, adds a run loop, and orchestrates multi-agent delegation
- Hierarchical task delegation: sub-tasks are additional responders in round-robin fashion; `Task.run()` has a uniform signature enabling recursive nesting
- Message-passing multi-agent: agents act as message transformers with three responder methods (LLM, Agent, User) per agent
- Tool/function-calling via Pydantic `ToolMessage` subclasses — no JSON schema writing required; Pydantic validation errors sent back to LLM for self-correction
- RAG via specialized `DocChatAgent` with vector-store retrieval, source-citation, and chunk re-ranking (RRF, diversity, periphery ranking)
- Batch execution: `run_batch_tasks` with async concurrency, `stop_on_first_result`, cost/token caps

## Key Features [coverage: low — 1 source]

- MCP Tools Support (v0.53.0): MCP server tools converted to Langroid `ToolMessage` instances
- `DocChatAgent`: PDF, DOCX, URL, dataframe ingestion; hybrid search; Crawl4AI browser-based crawling (v0.58.0)
- `SQLChatAgent`, `TableChatAgent`, `Neo4jChatAgent`: specialized domain agents for databases and knowledge graphs
- `TaskTool`: agents can spawn sub-agents with specific tools and configs (v0.56.0)
- Structured/JSON output with strict schema enforcement on compatible LLMs
- `@`-addressing: entities address other agents by name without a tool
- Infinite loop detection (cycle length <= 10, configurable)
- HTML Logger for interactive task visualization with collapsible entries (v0.57.0)
- Chainlit UI integration; Docker image available
- Message lineage/provenance tracking for observability
- Claude Code plugin: `langroid:patterns` and `langroid:add-pattern` skills

## Tech Stack [coverage: low — 1 source]

- Language: Python 3.11+
- Package: `langroid` on PyPI; modular extras (`doc-chat`, `db`, `hf-embeddings`, `all`)
- LLM providers: OpenAI, Anthropic, Google Gemini, Groq, Cerebras, Azure OpenAI, local via Ollama/oobabooga/LiteLLM, OpenRouter, Portkey AI Gateway (200+ models)
- Vector stores: Qdrant, Chroma, LanceDB, Pinecone, PostgresDB (PGVector), Weaviate
- Caching: Redis or Fakeredis (in-memory fallback)
- Build tooling: uv (moved from Poetry in v0.33.0); CI with pytest + codecov
- Docker image: `langroid/langroid` (multi-architecture)

## Traction [coverage: low — 1 source]

- 4,042 stars
- Created 2023-04-16; pushed 2026-06-15 — over 3 years of sustained development
- Production usage: Nullify (secure software dev/vulnerability management) selected Langroid over CrewAI, AutoGen, LangChain after evaluation
- Published in ML for Healthcare 2024 (pharmacovigilance multi-agent RAG system)
- Active release cadence: v0.59.0 (Pydantic V2 migration, 5–50x faster validation) in Aug 2025
- Discord community; Substack newsletter; Colab quick-start notebooks
- Consulting available from co-founders

## Use Cases [coverage: low — 1 source]

- Building production multi-agent pipelines with clear, inspectable message flow and lineage
- RAG applications: document Q&A, structured extraction from PDFs, contracts, reports
- Data Q&A: natural language to Pandas code (`TableChatAgent`) or SQL (`SQLChatAgent`)
- Knowledge graph reasoning via Neo4j or ArangoDB agents
- Research applications requiring structured information extraction with source citation
- Applications needing fine-grained developer control over agent interaction protocols

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — Microsoft's multi-agent framework; AutoGen is heavier and more opinionated on conversation patterns; Langroid's Task abstraction is simpler and more composable
- [[google_adk-python]] — Google's ADK uses a graph-based Workflow engine; Langroid uses hierarchical recursive task delegation with message passing
- [[camel-ai_camel]] — another research-origin multi-agent framework; CAMEL focuses on role-playing/society simulation, Langroid on practical RAG and tool-using agents
- [[pydantic_pydantic-ai]] — also Pydantic-first; pydantic-ai is newer and more minimalist, Langroid has deeper RAG, vector-store, and multi-agent tooling
- [[letta-ai_letta]] — memory-centric stateful agent platform; Langroid is a library (not a platform) with explicit developer control over state and orchestration

## Sources

- [[../../sources/github-langroid_langroid]]
