---
topic: trycua_cua
last_compiled: 2026-07-03
sources:
  - ../../sources/github-trycua_cua
status: active
---

# Cua

## Summary [coverage: low — 1 source]

Scraped 2026-07-01T02:45:27Z. Cua is open-source infrastructure for building, benchmarking, and deploying computer-use agents — AI agents that can control full desktops across macOS, Linux, Windows, and Android. It provides sandboxes, SDKs, and benchmarks under a unified Python API, enabling agents to see screens, click, type, and execute tasks autonomously. The project also includes Lume, a macOS virtualisation layer leveraging Apple's Virtualization.Framework for near-native VM performance on Apple Silicon, and Cua Drivers for background desktop automation without stealing cursor focus. Launched in January 2025, it reached 19 242 stars by July 2026 and remains actively maintained.

## Core Pattern [coverage: low — 1 source]

- Sandbox abstraction: a single `Sandbox` API wraps Linux containers, Linux VMs, macOS, Windows, and Android — deployable locally via QEMU or on cua.ai cloud, with BYOI support for custom images
- Background drivers: Cua Drivers expose a CLI and MCP server so coding agents (Claude Code, Cursor, Codex, etc.) can drive native desktop apps in the background without interrupting the user's session
- Benchmarking layer: Cua-Bench integrates OSWorld, ScreenSpot, and Windows Arena benchmarks with parallel execution and trajectory export for RL training
- Virtualisation substrate: Lume manages macOS/Linux VMs on Apple Silicon using Apple's Virtualization.Framework; Lumier provides a Docker-compatible interface over Lume
- MCP integration: Cua Drivers register as an MCP server, making desktop control a first-class tool for any MCP-compatible agent client

## Key Features [coverage: low — 1 source]

- Unified Python `Sandbox` API for Linux, macOS, Windows, and Android (local and cloud)
- Background computer-use via Cua Drivers on macOS and Windows (Linux pre-release), no cursor theft
- MCP server interface for wiring desktop control into Claude Code, Cursor, and other clients
- Benchmarking suite (OSWorld, ScreenSpot, Windows Arena) with parallel runs and trajectory export
- macOS VM management via Lume with near-native Apple Silicon performance
- Docker-compatible Lumier wrapper for Lume VMs
- Multi-touch gesture support for Android sandboxes
- Optional OmniParser integration for UI element parsing (CC-BY-4.0 licensed component)
- MIT licensed; optional `cua-agent[omni]` extension includes ultralytics (AGPL-3.0)

## Tech Stack [coverage: low — 1 source]

- Primary languages: Python (SDK); Swift (Lume/macOS virtualisation layer)
- Virtualisation: QEMU (local VMs), Apple Virtualization.Framework (Lume/Apple Silicon)
- Key optional dependencies: OmniParser (Microsoft, CC-BY-4.0), ultralytics (AGPL-3.0), Kasm (MIT)
- Deployment: local (QEMU) or cua.ai cloud; MCP transport via stdio
- Install: `pip install cua`; Lume and Cua Drivers via shell install scripts

## Traction [coverage: low — 1 source]

- 19 242 stars
- Created 2025-01-31; last pushed 2026-07-01 — very actively maintained
- Active Discord community; GitHub Sponsors programme active
- Listed on Trendshift repository rankings
- Hacktoberfest participant

## Use Cases [coverage: low — 1 source]

- Building autonomous desktop agents that interact with native GUI applications
- Giving coding agents (Claude Code, Cursor, Codex) background control of a local desktop without interrupting the user
- Evaluating computer-use model capabilities against OSWorld, ScreenSpot, and Windows Arena benchmarks
- Generating agent trajectories for reinforcement learning training data
- Running macOS VMs on Apple Silicon for CI, testing, or agent sandboxing
- Cross-platform desktop automation (macOS, Windows, Linux, Android) from a single Python API

## Related Frameworks [coverage: low — 1 source]

- [[e2b-dev_e2b]] — cloud sandboxes for code execution rather than full desktop/GUI control; complementary scope
- [[browser-use_browser-harness]] — browser-scoped computer use vs. Cua's full OS desktop control
- [[gptme_gptme]] — terminal-first agent with local tool execution; no dedicated VM/sandbox layer
- [[google_adk-python]] — general agent development kit without built-in sandbox or VM infrastructure
- [[nousresearch_hermes-agent]] — agent framework with browser/search tools; Cua provides the lower-level OS environment that such agents run inside

## Sources

- [[../../sources/github-trycua_cua]]
