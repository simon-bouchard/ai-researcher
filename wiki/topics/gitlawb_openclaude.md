---
topic: gitlawb_openclaude
last_compiled: 2026-07-03
sources:
  - ../../sources/github-Gitlawb_openclaude
status: active
---

# OpenClaude

## Summary [coverage: low — 1 source]

Scraped 2026-07-02T02:24:01Z. OpenClaude is an open-source, community-built coding-agent CLI forked from the Claude Code codebase and substantially extended to support multiple LLM providers and local model backends. It preserves the terminal-first coding-agent workflow — prompts, tool calls, MCP, slash commands, streaming output, sub-agents — while decoupling from Anthropic as the sole provider. With 29,654 stars and active July 2026 development, it is one of the most prominent open-source derivatives of Claude Code.

## Core Pattern [coverage: low — 1 source]

- Terminal-first interactive chat loop with full tool-use and sub-agent delegation
- Agent routing: per-agent model and provider overrides via `agentModels`/`agentRouting` config; built-in agents (verification, Explore, Plan) are individually routable
- Background sessions: long-running tasks detached from the terminal with `openclaude --bg`; session management via `openclaude ps/logs/kill`
- Conversation branching: resume, continue, or fork sessions by ID
- Headless gRPC server mode for embedding the engine in other applications or CI pipelines
- Sub-agent step limits: `maxSteps` in agent definitions caps tool-use steps and forces a summary

## Key Features [coverage: low — 1 source]

- Provider-agnostic: OpenAI-compatible APIs, Gemini, GitHub Models, Codex OAuth, Ollama, Atomic Chat, Fireworks AI, NEAR AI, Xiaomi MiMo, and more via `/provider` setup
- MCP (Model Context Protocol) support
- Slash commands including `/provider`, `/onboard-github`, `/model`
- Saved provider profiles in `.openclaude-profile.json`
- Web search via DuckDuckGo (free fallback) or Firecrawl for non-Anthropic providers
- Vision support: URL and base64 image inputs for compatible providers
- GitHub Copilot optimization: serialized sub-agent execution to conserve premium requests
- VS Code extension with provider-aware Control Center, in-editor chat, and Microsoft Foundry/Azure configuration
- AUR package for Arch Linux; Android install documented

## Tech Stack [coverage: low — 1 source]

- Language: TypeScript
- Runtime: Node.js >= 22.0.0; Bun 1.3.13+ for source builds
- Package: `@gitlawb/openclaude` on npm
- Build: Bun test runner, Bun build, smoke/doctor/privacy verification scripts
- Protocol: gRPC (headless server mode) with proto definitions in `src/proto/openclaude.proto`
- Not affiliated with or endorsed by Anthropic

## Traction [coverage: low — 1 source]

- 29,654 stars
- Created 2026-04-01; pushed 2026-07-02 — very active, approximately 3 months old at scrape time
- Sponsors: GitLawb, Bankr.bot, Atomic Chat, Xiaomi MiMo, Atlas Cloud
- Discord community; GitHub Discussions active
- AUR community-maintained package

## Use Cases [coverage: low — 1 source]

- Coding-agent workflows on non-Anthropic or local models (GPT-4o, Ollama, DeepSeek, Gemini, etc.)
- Teams or individuals who want Claude Code-style tooling without Anthropic API lock-in
- CI/CD pipelines needing a headless gRPC coding-agent engine
- Multi-provider setups where different sub-agents route to different models for cost optimization
- Local-model inference via Ollama with properly managed context windows

## Related Frameworks [coverage: low — 1 source]

- [[nousresearch_hermes-agent]] — another coding/agentic CLI; OpenClaude targets the same terminal-agent niche but with explicit multi-provider routing
- [[gptme_gptme]] — similar terminal-first agent CLI; gptme predates OpenClaude by 3 years and has a richer autonomous-agent ecosystem
- [[jackwener_opencli]] — complementary browser-to-CLI bridge that installs skills into agents like OpenClaude
- [[microsoft_autogen]] — framework-level multi-agent orchestration vs. OpenClaude's single-CLI approach
- [[strands-agents_harness-sdk]] — SDK-style agent harness; OpenClaude is end-user tooling rather than a developer SDK

## Sources

- [[../../sources/github-Gitlawb_openclaude]]
