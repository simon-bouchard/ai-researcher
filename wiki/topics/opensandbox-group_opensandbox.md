---
topic: opensandbox-group_opensandbox
last_compiled: 2026-07-03
sources:
  - ../../sources/github-opensandbox-group_OpenSandbox
status: active
---

# OpenSandbox

## Summary [coverage: low — 1 source]

Scraped 2026-07-02T02:24:16Z. OpenSandbox is a general-purpose sandbox platform for AI applications developed by Alibaba, providing secure isolated execution environments for coding agents, GUI agents, AI code execution, agent evaluation, and reinforcement learning training. It offers multi-language SDKs (Python, Java/Kotlin, TypeScript, C#/.NET, Go), a unified sandbox API defined by an open protocol, and Docker/Kubernetes runtimes for both local runs and large-scale distributed scheduling. Listed on the CNCF Landscape and carrying an OpenSSF Best Practices badge, it is positioned as production-grade infrastructure-layer tooling rather than an agent framework.

## Core Pattern [coverage: low — 1 source]

- Sandbox Protocol: defines lifecycle management and execution APIs as an OpenAPI spec, allowing custom runtime implementations to be plugged in
- Dual runtime targets: Docker for local development, Kubernetes for production-scale distributed scheduling; both managed through the same unified API
- Execution daemon (execd): handles command execution and file operations inside each sandbox instance, decoupled from the lifecycle server
- Ingress/egress network layer: unified ingress gateway with configurable routing strategies and per-sandbox egress controls at the boundary of each sandbox
- Credential Vault: secure credential injection for sandbox outbound requests without exposing secrets to workloads
- MCP integration: MCP server exposes sandbox operations (create, run commands, file I/O) to MCP-capable clients such as Claude Code and Cursor

## Key Features [coverage: low — 1 source]

- Multi-language SDKs: Python, Java/Kotlin, JavaScript/TypeScript, C#/.NET, Go
- `osb` CLI: terminal interface for sandbox creation, command execution, file operations, diagnostics, and egress policy management
- MCP server (`opensandbox-mcp`) for integration with MCP-capable AI clients
- Built-in sandbox environments: Command, Filesystem, and Code Interpreter
- Browser and desktop environments: Chrome + VNC, Playwright headless, full desktop (VNC), VS Code Web (code-server)
- Strong isolation: gVisor, Kata Containers, and Firecracker microVM support for workload/host isolation
- CNCF Landscape inclusion and OpenSSF Best Practices badge; E2E CI and Kubernetes nightly build CI
- Coding agent integrations: Claude Code, Gemini CLI, OpenAI Codex CLI, Qwen Code, Kimi CLI — each can run inside OpenSandbox
- Agent framework integrations: LangGraph, Google ADK, OpenClaw examples
- RL training support: DQN CartPole example; Harbor agent evaluation integration (one sandbox per trial)

## Tech Stack [coverage: low — 1 source]

- Primary language: Python (server, CLI, Python SDK, MCP server)
- Additional SDK languages: Java/Kotlin, JavaScript/TypeScript, C#/.NET, Go
- Sandbox server: Python FastAPI; configurable via TOML (~/.sandbox.toml)
- Secure runtimes: gVisor, Kata Containers, Firecracker microVM
- Runtime backends: Docker (local) and Kubernetes (production/distributed)
- Key tooling: uvx/uv for server invocation; Playwright and Chromium for browser environments
- Apache 2.0 license; developed by Alibaba (opensandbox-group organization on GitHub)

## Traction [coverage: low — 1 source]

- 11,763 stars on GitHub
- Active development: pushed 2026-07-02, one day before scrape
- Created 2025-12-17 — approximately 6.5 months to scrape date
- Listed in CNCF Landscape under orchestration/scheduling
- OpenSSF Best Practices certified
- Trending on Trendshift (repository #21828)
- Community: Discord (discord.gg/g7FuPs8YeD) and DingTalk groups

## Use Cases [coverage: low — 1 source]

- Running coding agent CLIs (Claude Code, Gemini CLI, OpenAI Codex, Qwen Code) in isolated sandbox environments
- Secure AI code execution with ephemeral, language-specific interpreters in isolated containers
- Browser automation and web scraping via Playwright or Chrome in sandboxes
- GUI agent workflows using a full desktop environment in a sandbox (VNC)
- Agent evaluation pipelines (e.g., Harbor framework, one sandbox per evaluation trial)
- Reinforcement learning training with isolated, checkpointed compute environments
- Remote development via VS Code (code-server) running in a sandbox
- Multi-agent orchestration backends requiring programmatic sandbox lifecycle management (LangGraph, Google ADK)

## Related Frameworks [coverage: low — 1 source]

- [[e2b-dev_e2b]] — most direct competitor: also a cloud sandbox runtime for AI code execution with multi-language SDKs; E2B is more managed-PaaS-oriented while OpenSandbox emphasizes self-hosted Kubernetes scale and stronger isolation options
- [[google_adk-python]] — agent development kit with a documented integration example for using OpenSandbox as the execution environment; ADK is the agent layer, OpenSandbox provides the sandbox infrastructure
- [[trycua_cua]] — focuses on computer-use agents with desktop GUI environments; OpenSandbox provides desktop and browser sandboxes as environment types within a broader platform
- [[nousresearch_hermes-agent]] — Hermes uses terminal backends (Docker, SSH, Modal) for execution isolation; OpenSandbox provides a more structured, protocol-defined sandbox layer with broader language SDK coverage
- [[microsoft_autogen]] — multi-agent orchestration framework that can use sandbox runtimes like OpenSandbox for code execution environments

## Sources

- [[../../sources/github-opensandbox-group_OpenSandbox]]
