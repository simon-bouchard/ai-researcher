---
concept: Persistent Agent Memory
last_compiled: 2026-07-03
topics_connected: [letta-ai_letta, zhayujie_cowagent, hkuds_nanobot, lsdefine_genericagent, nousresearch_hermes-agent, gptme_gptme, ruvnet_ruflo, aden-hive_hive, evomap_evolver, rightnow-ai_openfang, othmanadi_planning-with-files]
status: active
---

# Persistent Agent Memory

## Pattern

Persistent memory — the ability of an agent to recall information across sessions and build on past work — is implemented across 11+ tracked frameworks, but what's striking is the diversity of approaches. There is no consensus on *what* memory is or *how* it should persist: the same goal is served by structured key-value blocks (Letta), nightly dream distillation (CowAgent, nanobot), skill crystallization from task trajectories (GenericAgent, Hermes), git-tracked workspaces (gptme), HNSW vector databases (Ruflo), Gene/Capsule evolution stores (Evolver), file-based planning state (Planning with Files), role-scoped graph memory (Hive), and SQLite + vector hybrids (OpenFang).

The split isn't arbitrary — it reflects different theories of what an agent needs to remember. Letta frames memory as *structured state* (human context, persona): static facts injected into every session. CowAgent and nanobot frame it as *compressed experience*: raw conversation is too noisy, so a nightly process distills it into lasting memory entries. GenericAgent and Hermes frame it as *skill crystallization*: the execution path of a solved task is the memory worth keeping. Gptme frames it as *version-controlled workspace*: files are memory, git is the history. Planning with Files frames it as *task-execution continuity*: not memory in the rich sense, but enough state to survive a context wipe and resume work.

## Instances

- **2026-07-01** in [[../topics/letta-ai_letta]]: Memory blocks (`human`, `persona`, custom labels) as structured persistent state injected at runtime — memory as typed, server-managed schema rather than raw conversation history
- **2026-07-03** in [[../topics/zhayujie_cowagent]]: Three-tier memory (short-term → daily → MEMORY.md) with nightly Deep Dream distillation pass — memory as compressed, curated experience across timescales
- **2026-07-03** in [[../topics/hkuds_nanobot]]: Two-stage Dream memory with token-based management and auto-compact on idle — similar distillation pattern to CowAgent but with explicit token pressure as the trigger
- **2026-07-03** in [[../topics/lsdefine_genericagent]]: 5-layer memory (L0 Meta Rules → L4 Session Archive) with automated skill crystallization at L3 — task execution paths promoted to reusable SOPs
- **2026-07-03** in [[../topics/nousresearch_hermes-agent]]: Closed learning loop with FTS5 session search + LLM summarization for cross-session recall; skills created from complex tasks and improved during use; Honcho dialectic user modeling for personal profiling
- **2026-06-16** in [[../topics/gptme_gptme]]: Git-tracked workspace ("brain") as memory substrate — files are persistent state, commits are history, no separate memory database required
- **2026-07-03** in [[../topics/ruvnet_ruflo]]: AgentDB with HNSW indexing; SONA neural patterns route similar future tasks using learned trajectories; benchmarked 1.9x faster at N=20k vs brute force — vector memory as performance infrastructure
- **2026-07-01** in [[../topics/aden-hive_hive]]: Role-based memory scoped per agent role and evolving with project context across runs — memory partitioned by team structure rather than by topic or time
- **2026-06-16** in [[../topics/evomap_evolver]]: Gene/Capsule store in `<workspace>/.evolver/gep/` with EvolutionEvent audit trail — memory framed as an evolution asset rather than a recall database; backed by arXiv:2604.15097 showing Gene representation outperforms Skill docs
- **2026-07-02** in [[../topics/rightnow-ai_openfang]]: SQLite persistence + vector embeddings with canonical sessions and compaction — memory as standard database infrastructure rather than agent-specific abstraction
- **2026-07-01** in [[../topics/othmanadi_planning-with-files]]: `task_plan.md`, `findings.md`, `progress.md` on disk as execution-state memory; hook-driven re-injection before major decisions — memory as crash-proof planning continuity rather than knowledge recall

## What This Means

There is no single right answer for agent memory, and the tracked frameworks are discovering this experimentally. The implementations cluster around two fundamentally different purposes:

**Recall memory**: remembering facts, user preferences, and context across sessions (Letta blocks, gptme workspace, Hermes user modeling, OpenFang SQLite). These implementations answer "what does the agent know?" and are more like databases.

**Skill memory**: crystallizing successful execution patterns so they're reusable (GenericAgent L3, Hermes skills, Ruflo SONA routing, Evolver Gene/Capsules). These answer "how does the agent get better at tasks?" and are more like performance optimization.

**Distillation memory**: CowAgent and nanobot occupy a middle ground — they accumulate conversation history but run background processes to compress it into dense, durable entries. This mirrors how human memory consolidates during sleep.

The practical implication for anyone building agents: recall memory and skill memory require very different architectures. Conflating them (building one system that tries to do both) is probably why some agent "memory" features underperform — they optimize for the wrong kind of persistence.

The meta-insight: every framework above a certain capability threshold eventually adds some form of persistence. Memory is not optional for agents that operate across multiple sessions — it's the mechanism that turns a stateless chatbot into an agent with a history.

## Sources

- [[../topics/letta-ai_letta]]
- [[../topics/zhayujie_cowagent]]
- [[../topics/hkuds_nanobot]]
- [[../topics/lsdefine_genericagent]]
- [[../topics/nousresearch_hermes-agent]]
- [[../topics/gptme_gptme]]
- [[../topics/ruvnet_ruflo]]
- [[../topics/aden-hive_hive]]
- [[../topics/evomap_evolver]]
- [[../topics/rightnow-ai_openfang]]
- [[../topics/othmanadi_planning-with-files]]
