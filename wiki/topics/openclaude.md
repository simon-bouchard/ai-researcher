---
topic: openclaude
last_compiled: 2026-06-29
source_count: 1
status: active
---

# OpenClaude

## Summary [coverage: high — 1 source]

OpenClaude is an open-source coding-agent CLI built as a community fork of Claude Code, substantially modified to support multiple model providers beyond Anthropic. Its core value proposition is a single terminal-first workflow — prompts, tools, agents, MCP, slash commands, and streaming output — that works identically across cloud APIs and local inference backends. Users can switch providers without changing their workflow.

*Source scraped: 2026-06-16T03:25:18Z. Repository created 2026-04-01, last pushed 2026-06-16.*

## Core Pattern [coverage: high — 1 source]

OpenClaude follows the same agentic loop pattern as Claude Code: multi-step tool calling where the model drives a bash/file/grep/glob tool loop, executing sub-agents for specialized tasks (Explore, Plan, verification auditor). The key architectural extension is a settings-based **agent routing** system (`agentModels` + `agentRouting` in `~/.openclaude.json`) that allows different named agents to be dispatched to different model providers and endpoints — enabling cost optimization by running cheaper models for verification or exploration sub-tasks while a stronger model handles the main session. The parent-level provider is set interactively via `/provider`; per-agent overrides are handled by routing config independently. Sub-agent concurrency is configurable: by default, sub-agents run synchronously (serialized) when using GitHub Copilot to minimize premium request consumption, with env-var knobs to tune parallelism.

## Key Features [coverage: high — 1 source]

- **Multi-provider support**: OpenAI-compatible endpoints (OpenRouter, DeepSeek, Groq, Mistral, LM Studio), Gemini, GitHub Models, Codex (OAuth and CLI auth), Ollama (local, no API key), Fireworks AI (276 curated models), Xiaomi MiMo, NEAR AI, Atomic Chat, Bedrock/Vertex/Foundry, and the Gitlawb Opengateway smart gateway
- **MCP support**: built-in MCP tool integration carried over from Claude Code
- **Agent routing**: per-agent model/provider overrides via `~/.openclaude.json` — route the `verification` agent to a mini model, `Plan` to GPT-4o, and so on
- **Web search and fetch**: DuckDuckGo fallback for non-Anthropic models; optional Firecrawl integration for JS-rendered pages and reliable search
- **Headless gRPC server**: run OpenClaude as a gRPC service (`localhost:50051`) with bidirectional streaming for real-time text chunks, tool calls, and permission prompts — clients generatable in Python, Go, Rust from the `.proto` file
- **VS Code extension**: bundled in `vscode-extension/openclaude-vscode/` — launch integration, provider-aware Control Center, in-editor chat, theme support, and Azure OpenAI / Microsoft Foundry configuration via Secret Storage
- **Saved provider profiles**: guided setup via `/provider` slash command; credentials stored in user-level profiles
- **GitHub Copilot sub-agent optimization**: serializes sub-agent execution to reduce Premium Request consumption, with tuning vars (`GITHUB_COPILOT_MAX_SUBAGENTS`, `GITHUB_COPILOT_ALLOW_SUBAGENTS`, etc.)
- **Vision**: URL and base64 image inputs for providers that support it
- **Android install**: documented Android installation path

## Tech Stack [coverage: high — 1 source]

- **Primary language**: TypeScript
- **Runtime**: Node.js >= 22.0.0 (npm install); Bun 1.3.13+ for source builds and local development
- **Build**: Bun (`bun run build` outputs `dist/cli.mjs`)
- **Testing**: Bun's built-in test runner; coverage via `bun run test:coverage` with HTML heatmap output
- **Distribution**: npm package `@gitlawb/openclaude`; also available as an AUR package for Arch Linux
- **gRPC**: protobuf-defined service at `src/proto/openclaude.proto`
- **Optional dependencies**: ripgrep (system-wide, for grep tool), Firecrawl (optional, for enhanced web tools)
- **Deployment model**: CLI tool, local install; headless gRPC server mode for CI/CD or custom UI integration
- **License**: MIT (for OpenClaude contributors' modifications); derived Claude Code portions remain Anthropic's

## Traction [coverage: high — 1 source]

- **28,958 stars** — exceptionally high for a repo created 2026-04-01 (less than 3 months old at scrape time); indicates rapid community adoption
- Active development: last pushed 2026-06-16, same day as scrape
- Community channels: GitHub Discussions, GitHub Issues, Discord server, X/Twitter (@gitlawb)
- Sponsors: GitLawb, Bankr.bot, Atomic Chat, Xiaomi MiMo, Atlas Cloud — commercial backing across five organizations
- CI: PR Checks workflow via GitHub Actions
- Mirrored to GitLawb platform (gitlawb.com)
- Arch Linux AUR package maintained by community

## Use Cases [coverage: medium — 1 source]

- **Multi-provider coding assistance**: teams or individuals who want Claude Code-style agentic coding but with flexibility to run OpenAI, Gemini, DeepSeek, Ollama, or other providers — e.g., cost management by routing to cheaper models for sub-tasks
- **Local/private inference**: developers who need fully local operation via Ollama or Atomic Chat with no API key or data leaving the machine
- **CI/CD integration**: headless gRPC server mode enables embedding agentic tool-use capabilities (bash, file editing) into pipelines or custom UIs
- **Cost-optimized agent workflows**: agent routing lets users send expensive planning steps to strong models and cheap verification to mini models
- **GitHub Copilot users**: serialized sub-agent mode minimizes Premium Request burn while maintaining full agentic capabilities

## Related Frameworks [coverage: medium — 1 source]

- **Claude Code (Anthropic)**: the upstream codebase OpenClaude forked from; OpenClaude diverges by adding multi-provider support and removing the Anthropic-only constraint. OpenClaude is explicitly not affiliated with or endorsed by Anthropic.
- **OpenCode**: shares an API gateway option (OpenCode Zen/Go) and is referenced as a compatible provider endpoint; similar multi-provider CLI concept in the Go ecosystem
- **Codex CLI**: referenced as an auth source (`CODEX_CLI` credential path); a peer coding-agent CLI from OpenAI that OpenClaude can use as an auth backend
- **Continue.dev / Cursor**: VS Code-integrated coding assistants; OpenClaude occupies a similar niche but is terminal-first with an optional VS Code extension rather than a native IDE plugin
- **Aider**: another terminal-first multi-provider coding agent; OpenClaude differentiates with Claude Code's tool-loop architecture, MCP support, and gRPC server mode

## Sources [coverage: high — 1 source]

- [[../../sources/github-Gitlawb_openclaude]]
