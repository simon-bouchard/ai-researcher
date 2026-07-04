---
topic: waooai_waoowaoo
last_compiled: 2026-07-03
sources:
  - ../../sources/github-waooAI_waoowaoo
status: active
---

# waoowaoo AI Film Studio

## Summary [coverage: low — 1 source]

Scraped 2026-07-02T02:24:11Z. waoowaoo is a TypeScript-based AI-driven short drama and comic video production platform that automates the full creative pipeline from novel text to finished video. It is self-described as the industry's first professional AI agent platform for controllable film and video production, targeting Hollywood-standard workflows for shorts through live-action. As of scraping, the project is in early beta maintained by a small core team iterating rapidly; it launched in January 2026 and reached 13 020 stars by July 2026.

## Core Pattern [coverage: low — 1 source]

- Text-to-video pipeline: ingests novel or script text, extracts characters, scenes, and plot beats automatically, then produces storyboards and synthesised video output
- Task queue architecture: background jobs managed via Redis + BullMQ decouple heavy AI generation tasks (image, video, voice) from the web frontend
- Containerised deployment: full stack ships as Docker Compose services (Next.js app, MySQL, Redis, MinIO object storage), with a prebuilt image for zero-config startup
- Settings-driven AI provider: API keys for AI backends are configured at runtime via an in-app settings centre; the platform calls official provider APIs rather than bundling a model
- Multi-language UI: Chinese/English interface switchable at runtime, targeting both domestic and international markets

## Key Features [coverage: low — 1 source]

- AI script analysis: auto-parses novel input to extract characters, scenes, and plot structure
- AI character and scene generation: produces consistent character images and scene assets across shots
- Storyboard and video synthesis: auto-generates shot breakdowns and composes final video
- AI voice-over: multi-character speech synthesis for automated dubbing
- Docker-based self-hosting with prebuilt image pull or full source build options
- Optional HTTPS via Caddy to unlock full browser parallel connection limits
- Prisma ORM schema management with `prisma db push` for initialisation

## Tech Stack [coverage: low — 1 source]

- Primary language: TypeScript
- Frontend/Framework: Next.js 15 + React 19
- Database: MySQL via Prisma ORM
- Queue: Redis + BullMQ
- Object storage: MinIO
- Styling: Tailwind CSS v4
- Auth: NextAuth.js
- Deployment: Docker Compose (prebuilt image at `ghcr.io/saturndec/waoowaoo`)

## Traction [coverage: low — 1 source]

- 13 020 stars
- Created 2026-01-22; last pushed 2026-07-01 — very new project, actively maintained
- Beta waitlist active at waoowaoo.com; community feedback via GitHub Issues
- Solo-developer origin with core team now involved; external PRs reviewed for ideas but not merged directly

## Use Cases [coverage: low — 1 source]

- Rapid production of short-drama series from novel or script source material
- Comic/manga-style video content generation for social platforms
- Solo creators or small studios needing end-to-end AI assistance without manual storyboarding or asset creation
- Teams wanting a self-hosted, private AI film production environment

## Related Frameworks [coverage: low — 1 source]

- [[gptme_gptme]] — general-purpose agent CLI; waoowaoo targets a specific vertical (film/video) rather than open-ended agentic tasks
- [[camel-ai_camel]] — multi-agent framework for general task automation; waoowaoo uses a task-queue model for a fixed production pipeline rather than agent-to-agent coordination
- [[transformeroptimus_superagi]] — autonomous agent platform with multi-step task execution; waoowaoo is domain-specific to creative media production workflows
- [[activepieces_activepieces]] — general-purpose AI workflow automation platform; waoowaoo is a domain-vertical application rather than a horizontal automation tool

## Sources

- [[../../sources/github-waooAI_waoowaoo]]
