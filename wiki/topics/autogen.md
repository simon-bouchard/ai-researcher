---
topic: autogen
last_compiled: 2026-06-29
source_count: 1
status: active
---

# AutoGen

## Summary [coverage: high — 1 source]

AutoGen is a Microsoft Research-originated programming framework for building multi-agent AI applications that can act autonomously or work alongside humans. Its key value proposition is a layered, extensible design that lets developers work at different levels of abstraction — from a high-level AgentChat API for rapid prototyping down to a low-level Core API for event-driven, distributed agent runtimes.

**Important status note (as of scraped_at: 2026-06-16T03:10:22Z):** AutoGen is now in **maintenance mode**. It will not receive new features or enhancements and is community-managed going forward. Microsoft's official successor is the [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) (MAF), described as the enterprise-ready evolution of AutoGen with stable APIs and long-term support. Existing users are directed to the [AutoGen → MAF migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/).

## Core Pattern [coverage: high — 1 source]

AutoGen is built around a three-layer architecture:

- **Core API** (`autogen-core`): Implements message passing and event-driven agent execution. Supports both local and distributed runtimes. Cross-language: Python and .NET are both first-class targets.
- **AgentChat API** (`autogen-agentchat`): Opinionated higher-level API for rapid prototyping. Provides common multi-agent patterns including two-agent chat and group chats. Closest in feel to the earlier AutoGen v0.2 interface.
- **Extensions API** (`autogen-ext`): First- and third-party extension ecosystem that expands framework capabilities. Includes concrete LLM client implementations (OpenAI, AzureOpenAI) and capabilities such as code execution and MCP tool integration.

The primary agent abstraction is `AssistantAgent`. Multi-agent orchestration is achieved by wrapping agents as `AgentTool` instances and passing them as tools to a coordinating agent — agents calling agents through the standard tool-calling interface. Streaming is supported natively via `run_stream`.

## Key Features [coverage: high — 1 source]

- **MCP support**: First-class integration via `McpWorkbench` and `StdioServerParams` in `autogen-ext`. Any stdio-based MCP server (e.g., Playwright MCP) can be attached to an agent as a workbench of tools. Multiple MCP servers can be composed in a list.
- **No-code GUI (AutoGen Studio)**: Installed separately via `pip install autogenstudio`, runs as a local web app (`autogenstudio ui --port 8080`). Intended for rapid prototyping and demo purposes — explicitly not production-ready.
- **Benchmarking suite (AutoGen Bench / agbench)**: Dedicated package for evaluating agent performance against standardized tasks.
- **Cross-language runtime**: Core API supports both Python and .NET, with separate NuGet packages (`Microsoft.AutoGen.Core`, `Microsoft.AutoGen.Core.Grpc`, `Microsoft.AutoGen.RuntimeGateway.Grpc`).
- **Distributed runtime**: Core API supports distributed agent deployments beyond single-process execution.
- **Magentic-One**: A showcase multi-agent team built on AgentChat + Extensions APIs, capable of web browsing, code execution, and file handling. Demonstrates the framework's composability.
- **Streaming output**: `run_stream` + `Console` UI utility for real-time token streaming in terminal applications.

## Tech Stack [coverage: high — 1 source]

- **Primary language**: Python (requires Python 3.10+); .NET also supported at the Core API level
- **Package distribution**: PyPI (`autogen-core`, `autogen-agentchat`, `autogen-ext`, `autogenstudio`); NuGet for .NET packages
- **LLM clients**: OpenAI and AzureOpenAI via `autogen-ext`; other models referenced in documentation
- **MCP integration**: stdio-based MCP servers via `autogen-ext.tools.mcp`
- **Deployment model**: Self-hosted; local runtime by default, distributed runtime available through Core API
- **License**: MIT (code), Creative Commons Attribution 4.0 (documentation)

## Traction [coverage: high — 1 source]

- **Stars**: 58,979 — exceptionally high, placing AutoGen among the most-starred agent frameworks on GitHub
- **Origin**: Microsoft Research — strong institutional pedigree that drove significant early adoption
- **Activity**: Last pushed 2026-04-15, though in maintenance mode; active community via Discord and GitHub Discussions
- **Community channels**: Discord (`aka.ms/autogen-discord`), Twitter/X (`@pyautogen`), LinkedIn company page, GitHub Discussions
- **Ecosystem signal**: Has its own topic tag `autogen-ecosystem` on GitHub, indicating a broader plugin/extension community formed around the framework
- **Successor signal**: Microsoft is actively redirecting new users to Microsoft Agent Framework, which itself builds on AutoGen's design lessons — confirming AutoGen's historical influence on the field

## Use Cases [coverage: medium — 1 source]

- **Rapid prototyping of multi-agent workflows**: AgentChat API and AutoGen Studio are explicitly positioned for this
- **Research and experimentation**: Pioneered multi-agent orchestration patterns that influenced the broader community; still relevant for reproducing or extending prior research
- **Web automation**: Via MCP + Playwright integration (demonstrated in quickstart)
- **Code execution pipelines**: Extensions API includes code execution capabilities; Magentic-One demonstrates file handling + code execution
- **Cross-language agent systems**: .NET + Python polyglot deployments via the distributed Core API
- **Not recommended for**: Greenfield production deployments — Microsoft explicitly directs new production users to Microsoft Agent Framework

## Related Frameworks [coverage: medium — 1 source]

- **Microsoft Agent Framework (MAF)**: The direct successor. Enterprise-ready, stable APIs, long-term support, A2A and MCP interoperability. AutoGen's architecture and lessons are the explicit foundation for MAF. Migration guide available.
- **LangGraph / LangChain**: Competing Python-native multi-agent frameworks with their own graph-based orchestration patterns; AutoGen's event-driven, message-passing Core API offers a different model.
- **CrewAI**: Another popular multi-agent framework focused on role-based agent crews; AutoGen's `AgentTool` pattern (agents as tools) provides a different compositional primitive.
- **Semantic Kernel**: Also from Microsoft, focused on plugin/skill-based LLM orchestration; AutoGen and Semantic Kernel coexisted in Microsoft's AI tooling portfolio before MAF unified direction.
- **Magentic-One**: Not a competing framework but a reference multi-agent implementation built on AutoGen that demonstrates the framework's ceiling for complex task performance.

## Sources [coverage: high — 1 source]

- [[../../sources/github-microsoft_autogen]]
