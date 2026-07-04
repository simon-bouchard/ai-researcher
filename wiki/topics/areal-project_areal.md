---
topic: areal-project_areal
last_compiled: 2026-07-03
sources:
  - ../../sources/github-areal-project_AReaL
status: active
---

# AReaL

## Summary [coverage: low — 1 source]

Scraped 2026-06-16T03:10:37Z. AReaL (A Large-Scale Asynchronous Reinforcement Learning System) is an RL infrastructure designed to bridge foundation model training with modern agent-based applications, developed by researchers from Tsinghua IIIS and the AReaL Team at Ant Group. It is built on a fully asynchronous RL training paradigm optimized for efficiency and scalability, particularly for training large-scale reasoning and agentic models. AReaL's mission is to make building AI agents accessible, efficient, and cost-effective for a broad community of developers and researchers.

## Core Pattern [coverage: low — 1 source]

- Fully asynchronous RL training paradigm — decouples agent execution, reward calculation, and trajectory acquisition to enable multi-turn agentic RL without synchronization overhead.
- Supports both asynchronous and synchronous modes via a single `max_head_offpolicyness` setting.
- Agent integration via `base_url` replacement — any agentic runtime (OpenAI Agents SDK, CAMEL-AI, custom scaffoldings) can plug into AReaL's RL service without code changes.
- Dual-mode packaging: full AReaL for production-scale training and AReaL-lite (80% fewer lines of code, 90% of performance) for rapid prototyping and algorithm development.
- Training backends (Megatron, PyTorch FSDP, PyTorch Archon) and inference backends (vLLM, SGLang) are configurable and separable.

## Key Features [coverage: low — 1 source]

- Large algorithm library: GRPO, GSPO, PPO, DAPO, LitePPO, Dr.GRPO, REINFORCE++, RLOO, SAPO, M2PO, DPO, RLHF Reward Modeling, SFT, Distillation.
- Multi-turn and agentic RL training support (math, tool-calling, customer service, search agents, VLMs).
- LoRA support for parameter-efficient training.
- Cloud deployment via SkyPilot (GCP, AWS, Kubernetes).
- Huawei Ascend NPU support (stable, actively maintained).
- Vision-language model (VLM) training support (Qwen2.5-VL, Qwen3-VL, Gemma 3).
- NVIDIA TensorRT-LLM Scaffoldings integration for agentic RL.
- Self-evolving data synthesis engine (AReaL-SEA) for large MoE models.
- Incremental/weekly minor releases with monthly major releases.

## Tech Stack [coverage: low — 1 source]

- **Language:** Python
- **Package management:** uv
- **Training backends:** Megatron, PyTorch FSDP, PyTorch Archon (FSDP2)
- **Inference backends:** vLLM, SGLang
- **Cluster orchestration:** Ray
- **Deployment:** SkyPilot (cloud), local single-node
- **Key dependencies:** flash-attention, pre-commit, Hugging Face transformers
- **Hardware:** CUDA GPUs (primary), Huawei Ascend NPU (supported)

## Traction [coverage: low — 1 source]

- **Stars:** 5,306
- **Last push:** 2026-06-15
- **Created:** 2025-02-24
- Active biweekly community meetings (WeChat group + GitHub Discussions).
- CAMEL-AI's SETA terminal agent trained using AReaL.
- ASearcher (state-of-the-art search agent) built on AReaL's async RL.
- 235B MoE model via AReaL-SEA reported to surpass GPT-5 on tau2-bench.
- Actively hiring interns and full-time employees (US and China).
- OpenSSF Best Practices badge obtained.

## Use Cases [coverage: low — 1 source]

- Training large reasoning models (math, coding) via RL at scale.
- Multi-turn agentic RL training (tool use, customer service, search).
- Fine-tuning LLMs with RLHF reward modeling.
- Parameter-efficient training with LoRA on reasoning tasks.
- Integrating any existing agentic framework into an RL training loop via base_url replacement.
- Training vision-language models with RL.
- Large-scale MoE model RL training with Megatron or PyTorch Archon.

## Related Frameworks [coverage: low — 1 source]

- [[microsoft_autogen]] — multi-agent orchestration framework; AReaL focuses on RL training infrastructure rather than agent conversation patterns.
- [[camel-ai_camel]] — agent framework with built-in AReaL integration for agentic RL training; AReaL provides the RL backend, CAMEL provides the agent runtime.
- [[letta-ai_letta]] — persistent stateful agent serving platform; AReaL targets model training rather than deployment and memory management.
- [[google_adk-python]] — agent development kit for building and deploying agents; AReaL is RL training infrastructure, not an agent authoring SDK.

## Sources

- [[../../sources/github-areal-project_AReaL]]
