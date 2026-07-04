---
topic: can1357_oh-my-pi
last_compiled: 2026-07-03
sources:
  - ../../sources/github-can1357_oh-my-pi
status: active
---

# Oh My Pi (omp)

## Summary [coverage: low — 1 source]

Scraped 2026-07-02T02:24:09Z. Oh My Pi (`omp`) is a terminal-first AI coding agent that integrates IDE-level tooling — LSP, DAP debugger, subagents, persistent code execution, and hash-anchored edits — directly into the agent harness. It is a fork of Pi by Mario Zechner, extended into a batteries-included coding surface with 40+ provider integrations, 32 built-in tools, and a ~55k-line Rust core that keeps all hot-path operations in-process. The value proposition is a measurably better tool harness: benchmarks show up to 10x lift on edit accuracy for models like Grok Code Fast 1 and 61% fewer output tokens for Grok 4 Fast, while remaining fully open source (MIT) and extensible.

## Core Pattern [coverage: low — 1 source]

- **Terminal TUI as primary surface:** The agent runs interactively in a terminal with card-based tool rendering and preview-before-apply edit flow; the same engine is accessible as a one-shot CLI (`omp -p`), Node SDK, NDJSON RPC, or ACP (Agent Client Protocol for editors like Zed).
- **Hash-anchored edits (Hashline):** The `edit` tool uses content-hash anchors rather than line numbers or verbatim text, eliminating whitespace conflicts and stale-patch corruption; stale anchors are detected and rejected before disk writes.
- **In-process Rust core:** ~55k lines across four crates (`pi-natives`, `pi-shell`, `pi-ast`, `pi-iso`) implement search, shell, AST, PTY, and more as N-API addons — no fork/exec on the hot path, no dependency on external `rg`/`grep`/`bash` binaries.
- **Role-based model routing:** Work is routed by intent role (`default`, `smol`, `slow`, `plan`, `commit`) across 40+ providers with fallback chains, path-scoped model overrides, and round-robin credential rotation.
- **First-class subagents:** The `task` tool fans work out into isolated worktrees with schema-validated typed results returned to the parent; an `irc` tool enables short prose coordination between live agents in the same process.

## Key Features [coverage: low — 1 source]

- **LSP integration:** 14 LSP operations wired into every write — renames propagate through re-exports and barrel files before the file moves
- **DAP debugger:** 28 DAP operations — attaches lldb, dlv, or debugpy; steps, inspects frames, evaluates expressions
- **Persistent code execution:** `eval` runs persistent Python and Bun/JavaScript kernels with tool re-entry (agent tools callable from inside a running cell)
- **Advisor role:** A second model watches every turn and injects inline notes or blockers without sharing context with the main agent
- **Time-traveling stream rules:** Rules fire mid-token on regex match, inject a system reminder, and retry from the same point without paying context cost on every turn
- **Collab sessions:** `/collab` puts a live session on a relay with read-write or read-only link sharing; frames are sealed client-side
- **Hindsight memory:** `retain`/`recall`/`reflect` tools maintain a project-scoped SQLite memory bank across sessions
- **GitHub as filesystem:** PRs and issues resolve as paths (`pr://`, `issue://`) through the same `read` and `search` tools used for local files
- **Multi-format config inheritance:** On first run inherits rules from `.claude`, `.cursor`, `.windsurf`, `.gemini`, `.codex`, `.cline`, `.github/copilot`, `.vscode` — no migration
- **omp commit:** Splits uncommitted work into dependency-ordered atomic commits; rejects cycles before writing
- **Browser automation:** `browser` tool drives headless Chromium (stealth mode) or CDP-attached Electron apps (e.g. Slack)
- **AST-aware edits:** `ast_edit` performs structural rewrites via ast-grep with a preview/accept flow; `ast_grep` supports 50+ tree-sitter grammars
- **Conflict resolution:** merge conflicts become URLs (`conflict://N`); agent writes `@theirs`, `@ours`, or `@base` to resolve

## Tech Stack [coverage: low — 1 source]

- **Primary language:** TypeScript (agent runtime, TUI, SDK, extensions)
- **Rust core:** ~55k lines across `pi-natives`, `pi-shell`, `pi-ast`, `pi-iso` crates; exposed as N-API addon
- **Runtime:** Bun (≥1.2.14); also available via npm
- **Platforms:** macOS (x64/arm64), Linux (x64/arm64), Windows (x64); no WSL bridge required
- **Key dependencies (Rust):** tree-sitter / ast-grep-core, brush-shell (vendored embedded bash), ripgrep internals, syntect, portable-pty, tiktoken-rs, icy_sixel
- **Memory backend:** SQLite (via `@oh-my-pi/pi-mnemopi`)
- **Deployment:** Binary install (`omp.sh/install`), Homebrew, npm/bun global, or mise

## Traction [coverage: low — 1 source]

- **Stars:** 15,526
- **Last push:** 2026-07-02
- **Created:** 2025-12-31
- Active CI (GitHub Actions), npm package published (`@oh-my-pi/pi-coding-agent`)
- Changelog maintained; PR contribution requires a vouch system (gated pull requests)
- Discord community server (`discord.gg/4NMW9cdXZa`)
- Website with documentation at omp.sh; published benchmark comparisons across multiple models

## Use Cases [coverage: low — 1 source]

- Terminal-based agentic coding sessions requiring deep IDE integration (LSP renames, debugger attach, AST rewrites) without leaving the command line
- Multi-model workflows where different roles (planning, fast fan-out, deep reasoning) should route to different providers or subscription plans
- Large refactors and codebase exploration with parallel subagents working in isolated worktrees and returning typed structured results
- Debugging native or interpreted programs directly from the agent (lldb, dlv, debugpy) without manual print-statement iteration
- Teams wanting collaborative AI sessions with live link sharing (pair programming or read-only observation)
- Embedding a coding agent in a Node/TypeScript application via SDK, or driving it programmatically via NDJSON RPC or ACP from an editor
- Cross-provider usage without lock-in: users with subscriptions to Cursor, Copilot, Kimi Code, or similar coding plans can route through existing credentials

## Related Frameworks [coverage: low — 1 source]

- [[gptme_gptme]] — also a terminal-first coding agent with persistent sessions, but single-provider-focused and without Rust-native in-process tooling or LSP/DAP integration
- [[nousresearch_hermes-agent]] — agent harness emphasizing tool use and MCP; less focused on terminal UX or IDE-level code intelligence
- [[esengine_deepseek-reasonix]] — similarly a terminal coding agent distributed as a native binary; Go-based, DeepSeek-optimized, less IDE-integrated than omp
- [[strands-agents_harness-sdk]] — SDK-oriented agent harness for embedding agents in applications; overlaps with omp's Node SDK surface but without the interactive TUI layer
- [[microsoft_autogen]] — multi-agent orchestration framework; subagent fan-out is a shared concept but AutoGen targets programmatic orchestration rather than interactive terminal use

## Sources

- [[../../sources/github-can1357_oh-my-pi]]
