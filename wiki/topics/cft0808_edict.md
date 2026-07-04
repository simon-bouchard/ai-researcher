---
topic: cft0808_edict
last_compiled: 2026-07-03
sources:
  - ../../sources/github-cft0808_edict
status: active
---

# Edict (三省六部)

## Summary [coverage: low — 1 source]

Scraped 2026-07-01T02:48:33Z. Edict is a Python-based multi-agent orchestration system modeled on the Tang Dynasty's Three Departments and Six Ministries (三省六部) imperial governance structure, requiring OpenClaw as the underlying agent runtime. It coordinates 12 specialized AI agents through a mandatory review pipeline — planning, institutional review, dispatch, and parallel execution — with a real-time web dashboard (the "Grand Council Kanban") for monitoring, intervention, and audit. The framework's key differentiator is its mandatory veto-capable review layer (门下省/Menxia) that blocks task execution until plan quality is approved, combined with full observability and real-time task control.

## Core Pattern [coverage: low — 1 source]

- **Imperial hierarchy pipeline:** User ("Emperor") issues commands that flow through Taizi (triage) → Zhongshu (planning) → Menxia (review/veto) → Shangshu (dispatch) → six specialized ministries (parallel execution) → consolidated response.
- **Mandatory institutional review:** Every task must pass through Menxia (门下省), which can reject and force replanning; this is a non-optional architectural constraint, not a plugin.
- **Strict permission matrix:** Inter-agent messaging is governed by a hardcoded access-control table — agents can only send to explicitly permitted peers, enforcing separation of concerns.
- **Protected state machine:** Task lifecycle transitions (planning → review → dispatched → doing → done) are validated by `kanban_update.py` against a `_VALID_TRANSITIONS` table; illegal jumps are rejected and logged.
- **Async event bus:** Services communicate via Redis Streams EventBus with a transactional Outbox Relay guaranteeing at-least-once event delivery.

## Key Features [coverage: low — 1 source]

- 12-agent architecture: Taizi (triage), Zhongshu (planning), Menxia (review/veto), Shangshu (dispatch), plus six execution ministries (Hubu/data, Libu/docs, Bingbu/engineering, Xingbu/compliance, Gongbu/infra, Libu_hr/HR) and a daily briefing agent (Zaochao)
- Real-time "Grand Council" dashboard with 10 functional panels: Kanban, Monitor, Memorials (archive), Template Library (9 presets), Officials overview (token spend), News aggregation with Feishu push, Model config (hot-swap LLM per agent), Skills config, Sessions monitor, and daily Court Ceremony animation
- Task control: stop, cancel, and resume running tasks from the dashboard at any time
- Full audit trail: every state transition is logged; completed tasks archived as "memorials" with a five-stage timeline
- Hot LLM switching: each agent's model can be changed independently from the dashboard; changes apply in ~5 seconds via Gateway restart
- Remote Skills ecosystem: add capabilities to agents from GitHub URLs via dashboard UI, CLI (`skill_manager.py`), or REST API; supports version management
- DAG-based orchestration: Orchestrator Worker decomposes tasks into dependency graphs; Dispatch Worker handles parallel execution with exponential-backoff retry and resource locking
- Agent thinking visualization: real-time display of each agent's reasoning process, tool calls, and return values
- Zero-dependency backend: `server.py` (~2300 lines) uses Python stdlib `http.server` only
- Docker one-liner demo: `docker run -p 7891:7891 cft0808/sansheng-demo` with pre-loaded sample data
- LinUCB smart routing (`linucb_router.py`) and agent performance scoring ("功过簿") for cost optimization and model recommendation
- Court Discussion panel (朝堂议政): multi-agent LLM debate with department-perspective arguments, multi-round progression, and discussion archive

## Tech Stack [coverage: low — 1 source]

- **Language:** Python 3.10+ (backend); TypeScript + React 18 + Vite + Zustand (frontend, 13 components)
- **Agent runtime:** OpenClaw (required dependency; manages agent workspaces, gateway, sessions)
- **Backend:** Python stdlib only for `server.py`; SQLAlchemy + Redis for the async backend services (`edict/backend/`)
- **Event infrastructure:** Redis Streams (EventBus), transactional Outbox Relay
- **Deployment:** Docker / docker-compose; systemd service (`edict.service`) for production; one-click `install.sh` + `start.sh`
- **Messaging channels:** Feishu, Telegram, Signal (for issuing commands to agents)
- **Testing:** pytest-based e2e suite (`test_e2e_kanban.py`, 17 assertions) and state machine consistency tests

## Traction [coverage: low — 1 source]

- **Stars:** 16,132
- **Last push:** 2026-06-22
- **Created:** 2026-02-23
- Reached 16k+ stars within ~4 months of creation, indicating rapid community uptake
- README written primarily in Chinese (Simplified) with English and Japanese translations available
- Author maintains a WeChat public account (cft0808) for architectural deep-dives and project updates
- Phase 1 roadmap complete; Phase 2 (human-approval mode, message stream visualization, knowledge retrieval) in progress

## Use Cases [coverage: low — 1 source]

- Complex multi-step software development tasks requiring parallel specialist execution (e.g., designing a user auth system across API, DB, testing, and deployment documentation)
- Workflows where output quality must be institutionally reviewed and rejected before execution — not just human-in-the-loop but mandatory automated QA
- Teams wanting full audit trails and post-hoc replay of how a task was planned, reviewed, and executed
- Daily operational automation with news aggregation, scheduled briefings, and Feishu push notifications
- Organizations needing per-agent LLM cost control — different ministries can run cheaper models for routine tasks, expensive models for high-stakes review
- Pre-built workflow templates: weekly reports, code review, API design, competitive analysis, data reports, deployment plans, meeting summaries

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — also supports multi-agent conversation and human-in-the-loop, but lacks a mandatory institutional review stage, real-time Kanban, and task intervention controls
- [[camel-ai_camel]] — role-playing multi-agent framework focused on agent communication; no built-in veto/review layer or operational dashboard
- [[microsoft_agent-framework]] — Microsoft's agent framework with orchestration primitives; less opinionated about review governance and audit trails
- [[nousresearch_hermes-agent]] — single-agent CLI runner built on OpenClaw; Edict is the multi-agent, multi-ministry orchestration layer on top of the same OpenClaw runtime
- [[evomap_evolver]] — also built to run on OpenClaw; Evolver provides self-evolution/prompt governance for individual agents, while Edict provides multi-agent institutional orchestration

## Sources

- [[../../sources/github-cft0808_edict]]
