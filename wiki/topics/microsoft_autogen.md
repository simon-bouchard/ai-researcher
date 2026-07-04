---
topic: microsoft_autogen
last_compiled: 2026-07-03
sources:
  - ../../sources/github-microsoft_autogen
status: deprecated
---

# AutoGen

## Summary [coverage: low — 1 source]

Scraped 2026-06-16T03:10:22Z. **Maintenance mode as of 2026.** AutoGen is now community-managed and will not receive new features or enhancements; [[microsoft_agent-framework]] (MAF) is the designated enterprise-ready successor, with an official migration guide provided. Pioneered by Microsoft Research, AutoGen established foundational multi-agent orchestration patterns — conversational agent teams, group chats, and event-driven workflows — that strongly influenced the broader agentic AI ecosystem. Despite maintenance status it retains 58,979 stars, one of the highest counts in the tracked set, reflecting its historical significance.

## Core Pattern [coverage: low — 1 source]

- Layered architecture: Core API (message passing, event-driven agents, distributed runtime) → AgentChat API (opinionated rapid-prototyping layer) → Extensions API (first- and third-party integrations)
- Agents communicate via structured message passing; orchestration patterns include two-agent chat, group chats, and agent-as-tool composition via AgentTool
- Supports both autonomous and human-in-the-loop operation
- Cross-language runtime: Python and .NET implementations share the same Core API design
- MCP integration supported via McpWorkbench for connecting agents to external tool servers

## Key Features [coverage: low — 1 source]

- AssistantAgent: primary primitive for single-agent or multi-agent workflows
- AgentTool: wraps agents as callable tools, enabling hierarchical agent orchestration
- AutoGen Studio: no-code GUI for prototyping multi-agent workflows (explicitly not production-ready)
- AutoGen Bench: benchmarking suite for evaluating agent performance
- Magentic-One: reference multi-agent team built on AgentChat for web browsing, code execution, and file handling
- Extensions for OpenAI, AzureOpenAI, and third-party LLM clients
- Contributions now restricted to bug fixes, security patches, and documentation improvements only

## Tech Stack [coverage: low — 1 source]

- Primary language: Python (3.10+); also .NET
- PyPI packages: autogen-core, autogen-agentchat, autogen-ext, autogenstudio
- NuGet packages: Microsoft.AutoGen.Contracts, Microsoft.AutoGen.Core, Microsoft.AutoGen.Core.Grpc
- MCP support via autogen-ext tools integration
- MIT license (code); CC BY 4.0 (documentation)
- Community-managed going forward — no new Microsoft-led feature development

## Traction [coverage: low — 1 source]

- 58,979 stars — highest star count among all Microsoft-backed agent frameworks in the tracked set
- Last push: 2026-04-15 (last meaningful activity before maintenance mode declaration)
- Scraped 2026-06-16, approximately two months after last push
- Created 2023-08-18 — one of the older projects in the tracked set
- Discord and GitHub Discussions communities remain active but response times may vary under community-only maintenance

## Use Cases [coverage: low — 1 source]

- Existing AutoGen v0.2 deployments being maintained rather than actively developed
- Rapid prototyping of multi-agent patterns via AutoGen Studio (not for production deployment)
- Benchmarking and evaluating agent system performance via AutoGen Bench
- Educational reference for understanding foundational multi-agent conversation patterns
- Migration source: teams moving to [[microsoft_agent-framework]] using the official migration guide

## Related Frameworks [coverage: low — 1 source]

Successor: [[microsoft_agent-framework]] — enterprise-ready replacement with stable APIs, long-term support, A2A and MCP interoperability; migration guide at learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen.

- [[google_adk-python]] — Google's production agent SDK; analogous enterprise orientation to MAF (AutoGen's successor), different cloud ecosystem
- [[camel-ai_camel]] — contemporaneous multi-agent framework with role-playing focus; still actively developed unlike AutoGen
- [[pydantic_pydantic-ai]] — Python-only type-safe agent framework; actively maintained alternative for Python-only teams
- [[agentscope-ai_agentscope]] — multi-agent orchestration with graph-based patterns; research-oriented active alternative

## Sources

- [[../../sources/github-microsoft_autogen]]
