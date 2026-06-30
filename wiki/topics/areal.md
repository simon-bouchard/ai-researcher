---
topic: AReaL
last_compiled: 2026-06-29
source_count: 1
status: active
---

# AReaL

## Summary [coverage: high — 1 source]

AReaL (A Large-Scale Asynchronous Reinforcement Learning System) is a reinforcement learning infrastructure designed to bridge foundation model training with modern agent-based applications. Developed by researchers and engineers from Tsinghua IIIS and the AReaL Team at Ant Group, its key value proposition is making RL-based agent training **accessible, efficient, and cost-effective** through a fully asynchronous training paradigm that delivers industry-leading speed and scalability. AReaL targets the gap between general LLM training infrastructure and the specific demands of training reasoning and agentic models at scale.

Source scraped: 2026-06-16T03:10:37Z (repo last pushed 2026-06-15).

## Core Pattern [coverage: high — 1 source]

AReaL's central abstraction is **fully asynchronous RL training**: unlike synchronous systems (which stall training while waiting for rollouts), AReaL decouples trajectory generation from parameter updates, allowing continuous GPU utilization. The v0.3 "boba²" release demonstrated a **2.77× speedup** over synchronous baselines while matching or exceeding their training quality.

For agentic workloads, AReaL integrates with the **Scaffoldings** framework (NVIDIA TensorRT-LLM) to achieve a three-way decoupling of agent execution, reward calculation, and trajectory acquisition. This lets developers reuse existing agent modules and plug in any agentic runtime by simply replacing `base_url` and `api_key` — no code changes to the core training loop.

The system supports two deployment profiles:

- **AReaL** (full): production-grade, all parallelism strategies, intended for large-scale cluster training
- **AReaL-lite**: lightweight variant with an algorithm-first API, 80% fewer lines of code, 90% of performance — aimed at researchers and rapid prototyping

Both profiles support single-node and Ray cluster training.

## Key Features [coverage: high — 1 source]

**Algorithm breadth**: GRPO, GSPO, PPO, DAPO, LitePPO, Dr.GRPO, REINFORCE++, RLOO, SAPO, M2PO, DPO, RLHF reward modeling, SFT, and distillation — all supporting both asynchronous and synchronous modes via a `max_head_offpolicyness` flag.

**Training backends**:
- Megatron: ZeRO-1, tensor/sequence/context/pipeline/expert parallelism, LoRA, 1D sequence packing
- PyTorch FSDP (FSDP2): TP, SP, CP, LoRA, sequence packing
- PyTorch Archon: FSDP2 + full parallelism suite including expert parallel (no LoRA)

**Inference backends**: vLLM and SGLang, with data-parallel attention and expert parallel available on SGLang.

**Hardware**: CUDA (primary), Huawei Ascend NPU (actively maintained on `ascend` branch).

**Model support**: Qwen2/3, Qwen3-MoE, Qwen2.5-VL, Qwen3-VL, Gemma 3, and any Hugging Face LLM via PyTorch FSDP.

**Agentic integrations**: OpenAI Agents SDK, CAMEL-AI framework, Tongyi-DeepResearch search workflow.

**AReaL-SEA**: self-evolving data synthesis engine; combined with AReaL RL training, a 235B MoE model trained with it reportedly surpasses GPT-5 and achieves comparable performance to Gemini 3.0 Pro on τ²-bench.

**Cloud deployment**: SkyPilot integration for GCP, AWS, and Kubernetes.

**LoRA RL**: parameter-efficient training supported across FSDP and Megatron backends.

## Tech Stack [coverage: high — 1 source]

- **Primary language**: Python
- **Package manager**: uv
- **Training backends**: Megatron, PyTorch FSDP2, PyTorch Archon
- **Inference backends**: vLLM, SGLang
- **Distributed compute**: Ray cluster (optional; local single-node also supported)
- **Key dependencies**: flash-attn, transformers (Hugging Face)
- **Cloud**: SkyPilot (GCP, AWS, Kubernetes)
- **Hardware targets**: CUDA GPUs (primary), Huawei Ascend NPU
- **License**: Apache 2.0

Installation requires Python 3.12 and a pre-built flash-attn wheel to avoid source compilation.

## Traction [coverage: high — 1 source]

- **5,306 GitHub stars** as of scrape date (repo created 2025-02-24)
- **Very active**: weekly minor releases, monthly major releases; last commit 2026-06-15
- Academic paper published (arXiv 2505.24298, MLSys 2025 citation)
- Community biweekly meetings (launched 2026-04-18), WeChat group, GitHub Discussions
- **External adoption**: CAMEL-AI's SETA terminal agent was trained with AReaL; ASearcher (state-of-the-art search agent) built on AReaL's end-to-end async RL
- **Hiring**: actively recruiting interns and full-time employees in the US and China
- Backed by Tsinghua IIIS + Ant Group; collaboration with HKUST Relaxed System Lab and SGLang team
- OpenSSF Best Practices badge

## Use Cases [coverage: high — 1 source]

- **Reasoning model training**: math (GSM8K, Countdown), multi-turn math agents, coding agents
- **Agentic RL**: training agents that interact with external tools — search, customer service (τ²-bench retail/airline/telecom), tool-integrated reasoning (Python executor, calculator)
- **Vision-language model training**: geometry and visual reasoning tasks (Qwen2.5-VL, Qwen3-VL, Gemma 3)
- **RLHF alignment**: reward modeling on Anthropic HH-RLHF dataset, DPO
- **Black-box agent integration**: plug any existing agentic runtime into RL training by swapping `base_url` — no framework lock-in
- **Research prototyping**: AReaL-lite for fast iteration on new RL algorithms without full infrastructure overhead
- **Large-scale cluster training**: Megatron + expert parallelism for MoE models at 235B+ parameter scale

## Related Frameworks [coverage: medium — 1 source]

| Framework | Relationship |
|---|---|
| **ReaLHF** (OpenPsi Inc.) | Direct predecessor; AReaL evolved from ReaLHF's parameter-reallocation RLHF work |
| **OpenRLHF** | Alternative open-source RLHF training library; AReaL differentiates on async training and agentic focus |
| **VeRL** (volcengine) | Competing RL training system; also targets LLM post-training but with different architecture choices |
| **DeepScaleR / Open-Reasoner-Zero** | Community reasoning RL projects that AReaL acknowledges as pioneering work |
| **DAPO** (BytedTsinghua-SIA) | Algorithm implemented in AReaL; originating team is partly overlapping (Tsinghua affiliation) |
| **SGLang** | Inference backend integrated into AReaL; SGLang team contributed to AReaL-lite development |
| **CAMEL-AI / SETA** | Downstream consumer: SETA terminal agent uses AReaL for RL training |
| **OpenAI Agents SDK** | Integration target: AReaL provides an example for running agentic RL with the SDK |
| **NVIDIA Scaffoldings** | Modular agentic orchestration layer integrated into AReaL for decoupled execution/reward/trajectory |

AReaL's primary differentiator over OpenRLHF and VeRL is the **fully asynchronous training paradigm** and the explicit focus on **agentic multi-turn RL** — it treats agent runtime interoperability (any framework via `base_url`) as a first-class design goal rather than an afterthought.

## Sources [coverage: high — 1 source]

- [[../../sources/github-areal-project_AReaL]]
