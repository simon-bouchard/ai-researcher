Run the shell command: date -u +%Y%m%d%H%M
This gives today's date/time in UTC, formatted as YYYYMMDDHHMM. Use this as <end>.

Run the shell command: date -u -d "3 days ago" +%Y%m%d0000
This gives the date 3 days ago at 00:00 UTC, formatted as YYYYMMDDHHMM. Use this as <start>.

Fetch the arXiv API at:
http://export.arxiv.org/api/query?search_query=%28cat:cs.AI+OR+cat:cs.CL%29+AND+submittedDate:%5B<start>+TO+<end>%5D&sortBy=submittedDate&sortOrder=descending&max_results=300
(replace <start> and <end> with the computed timestamps; returns Atom XML)

For each returned paper, judge whether it falls in scope based on its title and abstract:

IN SCOPE: LLM agents and agent frameworks; agentic architectures and patterns (planning, memory, tool use, multi-agent systems); new open-source agent frameworks/libraries; research on agent-related topics.

OUT OF SCOPE: general ML/deep learning (vision, audio, etc.) unless agent-related; LLM training/fine-tuning research unless directly agent-related; hardware, infrastructure, MLOps.

Only proceed with papers that are clearly IN SCOPE.

For each in-scope paper, write a markdown file to /home/simon/documents/ai-researcher/sources/arxiv-<arxiv_id>.md (use the arXiv ID in the filename, replacing any "/" with "_"). Overwrite if it already exists. Use this exact structure:

---
title: "<paper title>"
arxiv_id: "<arxiv id>"
authors: ["<author1>", "<author2>", ...]
submitted: "<YYYY-MM-DD>"
updated: "<YYYY-MM-DD>"
categories: ["<cat1>", "<cat2>", ...]
primary_category: "<primary category>"
abs_url: "https://arxiv.org/abs/<arxiv_id>"
pdf_url: "https://arxiv.org/pdf/<arxiv_id>"
source: arxiv
scraped_at: "<current UTC timestamp, ISO 8601>"
---

<abstract text, verbatim>

Do not summarize, paraphrase, or add commentary beyond the in-scope/out-of-scope judgment — extraction and formatting only. If no papers are in scope, do nothing and respond [SILENT].
