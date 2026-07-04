---
topic: ruvnet_ruflo
last_compiled: 2026-07-03
sources:
  - ../../sources/github-ruvnet_ruflo
status: active
---

# Ruflo

## Summary [coverage: low — 1 source]

Scraped 2026-07-03T23:58:24Z. Ruflo (formerly Claude Flow) is a TypeScript agent meta-harness — an execution layer around Claude Code and OpenAI Codex — that adds swarm coordination, self-learning memory, cross-machine agent federation, and 100+ specialized agents on top of the underlying coding agent. Its core pitch: "Agent = Model + Harness; Ruflo is the harness." At 62,853 stars with pushes on the day of scraping, it is the highest-starred framework in this batch and claims 8.1M+ ecosystem downloads.

## Core Pattern [coverage: low — 1 source]

- Meta-harness pattern: sits above Claude Code/Codex and adds coordination, memory, and security rather than replacing the underlying LLM interaction
- Swarm topology: hierarchical, mesh, and adaptive topologies with queen-led consensus (Raft, Byzantine, Gossip)
- Self-learning loop: SONA neural patterns and ReasoningBank extract successful trajectories and route similar future tasks using learned patterns (claimed 89% routing accuracy)
- HNSW-indexed vector memory (AgentDB): persistent across sessions; benchmarked ~1.9x faster at N=20k vs brute force (recall@10 ~0.99)
- 27 lifecycle hooks auto-trigger background workers (audit, optimize, test gap detection, etc.)
- Goal-Oriented Action Planning (GOAP) with A* search through state spaces at goal.ruv.io

## Key Features [coverage: low — 1 source]

- 100+ specialized agents: coder, tester, security reviewer, architect, documentation generator, and domain-specific agents
- 35 Claude Code plugins organized by category: orchestration, memory/knowledge, intelligence/learning, code quality, security, DevOps, architecture/methodology, domain-specific
- Agent federation: zero-trust cross-machine collaboration via mTLS + ed25519; PII stripped before data leaves node; behavioral trust scoring; HIPAA/SOC2/GDPR audit trails
- Web UI beta at flo.ruv.io: multi-model chat with parallel MCP tool calling, ~210 tools, bring-your-own MCP servers, self-hostable via Docker
- MetaHarness: grades agent setup readiness (1-100), scans tool configs for security issues, detects regressions over time; `ruflo eject` converts project to standalone toolkit
- MCP server mode: `claude mcp add ruflo -- npx ruflo@latest mcp start`
- Multi-provider: Claude, GPT, Gemini, Cohere, Ollama with smart routing and failover
- WASM local agent sandbox (rvagent) + Anthropic Claude Managed Agents (cloud) via ruflo-agent plugin

## Tech Stack [coverage: low — 1 source]

- Primary language: TypeScript; Rust-based AI engine, embeddings, memory, and plugin system (Cognitum.One)
- Installation: `npx ruflo@latest init` (CLI) or `/plugin install ruflo-core@ruflo` (Claude Code plugin)
- Memory backend: AgentDB with HNSW indexing; RuVector for GPU-accelerated search and Graph RAG
- Web UI: Svelte frontend with MongoDB, Docker-deployable, also hosted at flo.ruv.io
- Two install paths: Claude Code plugin (lite — slash commands only, no MCP server) vs CLI init (full — hooks, daemon, MCP server, 98 agents)

## Traction [coverage: low — 1 source]

- 62,853 stars — highest-starred framework in this compiled batch
- Last pushed: 2026-07-03 (day of scrape) — extremely active
- Claims 8.1M+ ecosystem downloads and 106k git clones in 14 days
- Active Discord via Agentics Foundation; enterprise support at ruv.io
- Originated as "Claude Flow" and rebranded to Ruflo; powered by Cognitum.One architecture

## Use Cases [coverage: low — 1 source]

- Large engineering teams that want Claude Code to coordinate across multiple specialized agents rather than one generalist
- Projects requiring persistent cross-session memory and learned task routing
- Organizations needing cross-machine agent collaboration with compliance audit trails (HIPAA, SOC2, GDPR)
- Security-conscious deployments: AIDefence plugin, CVE scanning, PII-gated federation
- Financial and IoT domain use: ruflo-neural-trader and ruflo-iot-cognitum plugins

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — AutoGen is a Python multi-agent conversation framework; Ruflo is a TypeScript harness that wraps coding agents (Claude Code/Codex) specifically rather than building general agent conversations
- [[othmanadi_planning-with-files]] — Planning with Files is a lightweight file-based planning skill for any coding agent; Ruflo is a full harness adding memory, swarm, and federation; both target Claude Code but at very different scope
- [[nousresearch_hermes-agent]] — Hermes is one of the coding agents Ruflo can wrap; Ruflo explicitly supports Hermes integration in its plugin ecosystem
- [[letta-ai_letta]] — Letta specializes in long-term memory management; Ruflo includes HNSW vector memory as one of many components alongside swarm coordination and federation
- [[significant-gravitas_autogpt]] — AutoGPT provides a standalone autonomous agent platform with UI and marketplace; Ruflo is a coordination harness for developer-centric coding agents rather than an end-user product

## Sources

- [[../../sources/github-ruvnet_ruflo]]
