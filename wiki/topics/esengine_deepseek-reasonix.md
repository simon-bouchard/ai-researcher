---
topic: esengine_deepseek-reasonix
last_compiled: 2026-07-03
sources:
  - ../../sources/github-esengine_DeepSeek-Reasonix
status: active
---

# DeepSeek-Reasonix

## Summary [coverage: low — 1 source]

Scraped 2026-07-02T02:24:03Z. DeepSeek-Reasonix (Reasonix) is a DeepSeek-native AI coding agent for the terminal, distributed as a single static Go binary. It is engineered around DeepSeek's prefix-cache stability — context maintenance is a first-class design concern so token costs stay low across long sessions. Version 1.0 is a ground-up rewrite in Go (current default on `main-v2`); the earlier 0.x TypeScript releases are legacy and maintenance-only on the `v1` branch. Ranked Top 2 in Agents and Top 3 in CLI by velocity on oosmetrics.com.

## Core Pattern [coverage: low — 1 source]

- Config-driven harness: providers, the agent, enabled tools, and plugins are all declared in `reasonix.toml` — no hardcoded models.
- Multi-model composable execution: an executor and a planner model can run together in separate, cache-stable sessions; DeepSeek ships as a preset but any OpenAI-compatible endpoint is a config entry.
- Plugin architecture over stdio JSON-RPC (MCP-compatible): external tools run as subprocesses; built-in tools self-register at compile time.
- Cache-aware context loop: startup injects a stable environment summary, stale tool output is pruned before summary compaction, and tool schema is versioned for regression review.
- Snapshot-based edit safety net via checkpoints (`Esc-Esc` / `/rewind`).

## Key Features [coverage: low — 1 source]

- Single static Go binary (`CGO_ENABLED=0`), cross-compiled to six targets (darwin/linux/windows × amd64/arm64)
- `npm i -g reasonix` or `brew install` distribution; prebuilt archives with SHA256SUMS on every release
- `reasonix setup` config wizard generates `reasonix.toml`; `/init` generates `AGENTS.md` project memory file
- Two-model collaboration (executor + planner) with independent cache-stable sessions
- MCP-compatible plugin system via stdio JSON-RPC
- Permissions and sandbox layer configurable in `reasonix.toml`
- Slash commands, `@` file references
- IM bot integration: Feishu, Lark, WeChat — approvals, YOLO mode, and commands from IM
- Windows builds code-signed via SignPath Foundation
- Bilingual (English/Chinese) documentation and bilingual Discord community (`#help` / `#求助`)

## Tech Stack [coverage: low — 1 source]

- **Language:** Go (1.0+ rewrite); legacy 0.x was TypeScript
- **Distribution:** npm package (`reasonix`) wrapping a native binary; Homebrew tap on macOS
- **Config format:** TOML (`reasonix.toml`)
- **Key dependencies:** only a TOML parser (by design — zero-friction static binary)
- **LLM integration:** OpenAI-compatible HTTP endpoints; DeepSeek preset out of the box
- **Plugin protocol:** stdio JSON-RPC (MCP-compatible)

## Traction [coverage: low — 1 source]

- **Stars:** 25,626
- **Last push:** 2026-07-02
- **Created:** 2026-04-21
- Ranked Top 2 in Agents by velocity and Top 3 in LLMs and CLI by velocity (oosmetrics.com)
- ~25k stars in under 3 months, rapid growth trajectory
- Active Discord community with bilingual support channels
- Multiple named contributors; promoted on XiaoHongShu (AIGC Link)
- Also mirrored on AtomGit

## Use Cases [coverage: low — 1 source]

- Terminal-based AI coding assistance for developers using DeepSeek models
- Long-running agentic coding sessions where prefix-cache stability and cost control matter
- Teams wanting a config-file-driven agent harness with no vendor lock-in (any OpenAI-compatible endpoint)
- Multi-model workflows pairing a fast executor with a deeper planner model
- IM-integrated coding workflows via Feishu, Lark, or WeChat bot connectors

## Related Frameworks [coverage: low — 1 source]

- [[can1357_oh-my-pi]] — similarly a terminal coding agent distributed as a native binary; TypeScript/Rust-based with deeper IDE integration (LSP, DAP), more providers, and richer TUI
- [[gptme_gptme]] — similar terminal-based coding agent; Python-native rather than a single Go binary; no DeepSeek-specific cache optimisation
- [[nousresearch_hermes-agent]] — another CLI coding agent; uses o-series OpenAI models rather than DeepSeek; TypeScript-based
- [[strands-agents_harness-sdk]] — general-purpose agent harness SDK; library/SDK model rather than a standalone terminal binary
- [[the-pocket_pocketflow]] — lightweight agent framework focused on workflow composition rather than interactive terminal coding sessions

## Sources

- [[../../sources/github-esengine_DeepSeek-Reasonix]]
