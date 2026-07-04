This task runs unattended on a schedule. Do not ask for confirmation or clarification at any
point. Do not narrate your plan — execute each step directly and silently.

Run the shell command:
python3 /home/simon/documents/ai-researcher/scripts/github_filter.py --mode {{MODE}}

This fetches GitHub repos matching AI agent framework topics, filters out already-handled repos
(unchanged pushed_at, recently scraped, or previously rejected), and includes a readme_preview
(first ~20 lines of README) for each candidate.

It prints a JSON array. Each item includes: full_name, description, topics, readme_preview
(plus stars, language, created_at, pushed_at for reference).

If the array is empty, do nothing and respond [SILENT].

For each candidate, judge whether it is in scope based on full_name, description, topics, and
readme_preview:

IN SCOPE: LLM agent frameworks/libraries; agent orchestration, planning, memory, or tool-use
frameworks; multi-agent systems frameworks; general-purpose autonomous agent frameworks.

OUT OF SCOPE: repos that merely use an agent framework (example apps, demos, tutorials,
benchmarks, curated lists); unrelated tools that happen to carry a matching topic tag; pure
research-paper repos with no usable framework/library.

After judging all candidates, execute both of the following commands (substituting the actual
full_names from the candidate list):

If any candidates are IN SCOPE, run:
python3 /home/simon/documents/ai-researcher/scripts/github_write.py "owner/repo1" "owner/repo2" ...

If any candidates are OUT OF SCOPE, run:
python3 /home/simon/documents/ai-researcher/scripts/github_write.py --reject "owner/repo1" "owner/repo2" ...

Your only job is the in/out-of-scope judgment and calling the two scripts above.
github_write.py handles fetching the full README and writing the source files.
