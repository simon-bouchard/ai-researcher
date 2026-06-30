---
concept: Persistent Agent Memory
last_compiled: 2026-06-29
topics_connected: [letta, cowagent, genericagent, nanobot, hermes-agent]
status: active
---

# Persistent Agent Memory

## Pattern

Five frameworks in this tracker have built persistent memory as a core architectural primitive — not a plugin or afterthought, but the central design concern. Each has named it differently (MemGPT memory blocks, Dream memory, L0–L4 memory layers, FTS5 cross-session memory) and solved it differently, but all share the same root insight: stateless execution loops are insufficient for agents operating over long time horizons.

The approaches diverge sharply at the memory model level. Letta (the MemGPT successor) treats memory as addressable blocks that the agent can self-edit. GenericAgent uses a 5-tier hierarchy from volatile working memory to crystallized skill. Hermes-agent combines FTS5 full-text search with a Honcho user modeling layer. CowAgent adds a "Deep Dream" distillation pass that compresses episodic memories into long-term abstractions. Nanobot brands it "Dream memory" with a `/goal` mode for sustained objectives. Despite different architectures, all five are solving the same fundamental problem: how does an agent know what it has already done, learned, and decided?

## Instances

- **2024** in [[../topics/letta]]: MemGPT introduced self-editing memory blocks as the core primitive; Letta is its production successor with a full Agents API and hosted cloud option
- **2026-02** in [[../topics/cowagent]]: CowAgent v2.0 rebranded from chatgpt-on-wechat and added a three-tier memory system with "Deep Dream" distillation loop — persistent memory became the product's main identity
- **2026-01** in [[../topics/genericagent]]: GenericAgent launched with a 5-layer memory system (L0 volatile → L4 crystallized Skill) as the primary differentiator in its arXiv paper
- **2025-11** in [[../topics/nanobot]]: Nanobot shipped "Dream memory" and `/goal` sustained-objective mode as founding features, not v2 additions
- **2025-07** in [[../topics/hermes-agent]]: Hermes-agent added FTS5 cross-session memory and Honcho user modeling as part of its "closed learning loop" architecture

## What This Means

Persistent memory is the next frontier of differentiation in agent frameworks after tool-calling and multi-agent coordination. The frameworks that have committed to it earliest (Letta, Hermes) have built the most architecturally distinctive products. The ones adding it as a feature later risk being outcompeted on depth.

The open question is which memory model wins. Self-editing blocks (Letta) give the agent fine control but require careful engineering to avoid hallucinated edits. Distillation loops (CowAgent, GenericAgent) are more opaque but may produce better compression. FTS5 search (Hermes) is principled and inspectable. Watching which approach survives production use cases is the key signal to track.

## Sources
- [[../topics/letta]]
- [[../topics/cowagent]]
- [[../topics/genericagent]]
- [[../topics/nanobot]]
- [[../topics/hermes-agent]]
