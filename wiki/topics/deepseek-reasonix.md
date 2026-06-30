---
topic: DeepSeek-Reasonix
last_compiled: 2026-06-29
source_count: 1
status: active
---

# DeepSeek-Reasonix

## Summary [coverage: high — 1 source]

DeepSeek-Reasonix (package name: `reasonix`) is a DeepSeek-native AI coding agent for the terminal, engineered around prefix-cache stability to keep token costs low across long sessions. Its core value proposition is a config- and plugin-driven harness delivered as a single static Go binary — no runtime dependencies beyond a TOML parser — that stays cheap to run because it is explicitly tuned to DeepSeek's prefix cache behavior.

Version 1.0 is a ground-up rewrite in Go from the earlier 0.x TypeScript codebase. The Go branch (`main-v2`) is now the default; the TypeScript releases are legacy (maintenance-only on the `v1` branch). Installation still goes through npm (`npm i -g reasonix`) for cross-platform convenience, but the package now delivers the native Go binary.

Source scraped: 2026-06-16T03:25:22Z.

## Core Pattern [coverage: high — 1 source]

Reasonix is a terminal-resident coding agent driven by a `reasonix.toml` config file. The core orchestration model is a single agent loop that can optionally be split into a two-model setup: an executor model and a planner model running in separate, cache-stable sessions. This two-model collaboration is a first-class feature, not a workaround.

Key abstractions:

- **Config-driven providers:** every model, endpoint, and API key is declared in `reasonix.toml`. No models are hardcoded. Resolution order is flag > local config > user config > built-in defaults.
- **Plugin system (MCP-compatible):** external tools run as subprocesses over stdio JSON-RPC. Built-in tools self-register at compile time. The plugin interface is MCP-compatible, meaning existing MCP tool servers can be wired in as subprocesses.
- **Project memory via `AGENTS.md`:** running `/init` in a session generates an `AGENTS.md` file that captures project-level context, persisted across sessions.
- **Checkpoints and rewind:** a snapshot-based edit safety net allows rolling back file changes with Esc-Esc or the `/rewind` command.
- **Slash commands and `@` references:** interactive session controls for referencing files, running slash commands, and managing agent behavior.

## Key Features [coverage: high — 1 source]

- **MCP-compatible plugin system:** external tools communicate over stdio JSON-RPC using an MCP-compatible protocol, enabling reuse of existing MCP tool servers.
- **Two-model collaboration:** executor + planner can run in separate cache-stable sessions, optionally using different models (e.g., `deepseek-flash` for execution, `mimo-pro` for planning).
- **Multi-provider support:** DeepSeek (flash/pro) and MiMo ship as presets; any OpenAI-compatible endpoint is a single config entry. Provider switching is a config change, not a code change.
- **Prefix-cache stability:** the entire agent design is tuned around DeepSeek's prefix cache to keep token costs low across long-running sessions.
- **Checkpoint/rewind:** snapshot-based file edit safety net (`/rewind`, Esc-Esc).
- **Permissions and sandbox:** configurable permission model and sandbox, documented in the Guide.
- **IM bot integration:** Feishu, Lark, and WeChat bot connections from a desktop app, with support for approvals, YOLO mode, and commands from IM.
- **Pipe support:** stdin piping (`echo "explain this code" | reasonix run`) for scriptable non-interactive use.
- **Zero-friction distribution:** `CGO_ENABLED=0` single static binary; cross-compiles to six targets (darwin/linux/windows × amd64/arm64) with one command. Windows builds are code-signed via the SignPath Foundation.

## Tech Stack [coverage: high — 1 source]

- **Primary language:** Go (v1.0+). The earlier 0.x releases were TypeScript.
- **Configuration:** TOML (`reasonix.toml`). Only runtime dependency is a TOML parser.
- **Distribution:** npm package (`reasonix`) wrapping a prebuilt native Go binary; also available via Homebrew tap (`esengine/reasonix/reasonix`) and as direct GitHub release archives with SHA256SUMS.
- **Model interface:** OpenAI-compatible API protocol. DeepSeek and MiMo are bundled presets; any OpenAI-compatible endpoint is supported via config.
- **Plugin interface:** stdio JSON-RPC (MCP-compatible).
- **TUI:** terminal UI (topics include `tui` and `ink`, though `ink` is a Node.js TUI library — likely a legacy tag from the 0.x TypeScript era; the current Go rewrite uses its own TUI layer).
- **License:** MIT.

## Traction [coverage: high — 1 source]

- **22,345 GitHub stars** as of scrape date (2026-06-16), on a repository created 2026-04-21 — roughly 22k stars in under two months, indicating very rapid growth.
- **OOS Metrics rankings:** Top 2 in Agents by velocity, Top 3 in LLMs by velocity, Top 3 in CLI by velocity.
- **Active development:** last pushed 2026-06-16 (same day as scrape). Ongoing Go rewrite with a defined migration path from 0.x TypeScript.
- **Community:** Discord server (bilingual English/Chinese), Chinese community presence on XiaoHongShu, AtomGit mirror for Chinese developers, WeChat Pay donation channel.
- **Multiple contributors:** named acknowledgments list 9 contributors beyond the maintainer, with a contributor graph visible on GitHub.
- **npm downloads badge** present (exact count not in source), CI badge active.

## Use Cases [coverage: medium — 1 source]

- **Interactive coding sessions in the terminal:** primary use case — long-running terminal agent sessions where prefix-cache stability and low token cost matter.
- **Automated coding tasks:** `reasonix run "..."` for non-interactive task execution (implement TODOs, add tests, etc.).
- **Scripted/piped workflows:** stdin piping allows integration into shell scripts and CI pipelines.
- **Two-model agentic workflows:** executor + planner split for tasks requiring a reasoning model separate from an execution model.
- **IM-integrated coding:** Feishu/Lark/WeChat bot integration for teams using those platforms as their primary collaboration tool (prominent in Chinese enterprise contexts).
- **Self-hosted / cost-sensitive deployments:** the explicit prefix-cache optimization and DeepSeek-native design make it suited for teams trying to minimize API costs on long coding sessions.

## Related Frameworks [coverage: medium — 1 source]

- **Claude Code (Anthropic):** the closest direct analogue — a terminal-resident AI coding agent with a slash-command interface, project memory, permission/sandbox model, and MCP plugin support. Reasonix explicitly mirrors many of these patterns (AGENTS.md mirrors CLAUDE.md, `/rewind` mirrors Claude Code's checkpoint concept). Reasonix differentiates on DeepSeek-native prefix-cache tuning, Go binary distribution, and two-model collaboration.
- **Aider:** another terminal coding agent, but conversation/diff-centric rather than agent-loop-centric. Reasonix targets longer-running autonomous sessions; Aider is more interactive and patch-focused.
- **OpenHands (formerly OpenDevin):** browser-based sandboxed coding agent; heavier infrastructure vs. Reasonix's single binary + terminal model.
- **Goose (Block):** terminal coding agent built for extensibility via plugins, similar distribution model. Less DeepSeek-specific; broader provider support out of the box.
- **Amp (Sourcegraph):** terminal coding agent with MCP support. Commercial/cloud focus vs. Reasonix's self-hosted single-binary model.

## Sources [coverage: high — 1 source]

- [[../../sources/github-esengine_DeepSeek-Reasonix]]
