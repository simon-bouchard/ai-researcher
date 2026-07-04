---
topic: microsoft_agent-framework
last_compiled: 2026-07-03
sources:
  - ../../sources/github-microsoft_agent-framework
status: active
---

# Microsoft Agent Framework (MAF)

## Summary [coverage: low — 1 source]

Scraped 2026-07-03T23:58:22Z. Microsoft Agent Framework (MAF) is an open, multi-language framework for building production-grade AI agents and multi-agent workflows in Python and .NET, officially designated as the enterprise-ready successor to [[microsoft_autogen]]. It provides graph-based orchestration patterns (sequential, concurrent, handoff, group collaboration), built-in durability and checkpointing, human-in-the-loop control, and observability via OpenTelemetry, targeting teams moving agents from prototype to production. MAF integrates with Microsoft Foundry, Azure OpenAI, OpenAI, and the GitHub Copilot SDK, with Foundry Hosted Agents deployable with just two additional lines of code.

## Core Pattern [coverage: low — 1 source]

- Graph-based workflow orchestration: agents composed into directed graphs supporting sequential, concurrent, handoff, and group collaboration patterns
- Layered architecture: Agent primitives → Workflow orchestration → Hosting/deployment
- Pluggable provider model: swap LLM providers (Azure OpenAI, OpenAI, Foundry, others) without rewriting agent logic
- Middleware pipeline: flexible request/response processing, exception handling, and custom interceptors at the agent level
- Durable execution: checkpointing, restartability, streaming, human-in-the-loop, and time-travel built into the workflow layer
- Declarative agent definitions via YAML alongside imperative Python and C# APIs
- Agent-to-Agent (A2A) interoperability and MCP integration

## Key Features [coverage: low — 1 source]

- Full Python and C#/.NET support with consistent APIs across both languages
- Multi-provider LLM support: Azure OpenAI, OpenAI, Microsoft Foundry, and others
- Graph-based workflows with checkpointing, streaming, human-in-the-loop control, and time-travel
- Foundry Hosted Agents: deploy to Foundry-hosted infrastructure with 2 additional lines of code
- Built-in OpenTelemetry integration for distributed tracing and observability
- Declarative agents defined in YAML for faster setup and versioning
- Agent Skills: domain-specific knowledge bases built from files, inline code, or class libraries
- AF Labs: experimental packages for benchmarking, reinforcement learning, and research
- DevUI: interactive developer UI for agent development, testing, and debugging
- Official migration guides from both AutoGen and Semantic Kernel

## Tech Stack [coverage: low — 1 source]

- Primary languages: Python, C#/.NET
- Python package: `agent-framework` on PyPI; .NET: `Microsoft.Agents.AI` on NuGet
- Cloud integrations: Microsoft Foundry, Azure OpenAI, Azure Functions, Durable Task
- Auth: Azure Identity (DefaultAzureCredential, ManagedIdentityCredential)
- Observability: OpenTelemetry
- Deployment: local development, Azure Functions, Durable Agents/Workflows, Foundry-hosted agents

## Traction [coverage: low — 1 source]

- 11,852 stars on GitHub
- Very active development: pushed 2026-07-03, same day as scrape
- Created 2025-04-28 — rapid growth as the designated AutoGen successor
- Official MS Learn documentation (learn.microsoft.com/en-us/agent-framework/) and blog (devblogs.microsoft.com/agent-framework)
- Microsoft Foundry Discord community with weekly public office hours
- Inherits AutoGen's large user base (58,979 stars) via official migration path

## Use Cases [coverage: low — 1 source]

- Production multi-agent pipelines requiring durability, restartability, and observability
- Enterprise workflows needing governance, human-in-the-loop control, and long-term Microsoft support
- Cross-language teams building agents in both Python and .NET on shared infrastructure
- Azure-native deployments integrating with Microsoft Foundry or Azure OpenAI
- Teams migrating from AutoGen or Semantic Kernel seeking stable APIs and long-term support
- Research and experimentation via AF Labs (benchmarking, reinforcement learning)

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — direct predecessor; now in maintenance mode with Microsoft directing all new users to MAF; MAF adds enterprise-grade stability, A2A/MCP interoperability, and long-term support
- [[google_adk-python]] — Google's analogous production agent SDK; similar enterprise orientation but Google Cloud-native rather than Azure/Microsoft ecosystem
- [[agentscope-ai_agentscope]] — multi-agent orchestration with graph-based patterns; research-oriented vs. MAF's production/enterprise focus
- [[pydantic_pydantic-ai]] — Python-only agent framework with strong type safety; narrower scope than MAF's dual-language, cloud-hosted offering
- [[strands-agents_harness-sdk]] — AWS-oriented agent SDK; similar enterprise positioning but different cloud ecosystem

## Sources

- [[../../sources/github-microsoft_agent-framework]]
