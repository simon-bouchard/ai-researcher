#!/usr/bin/env python3
import sys, json, urllib.request, os

def in_scope(repo):
    topics = repo.get('topics', [])
    desc = (repo.get('description') or '').lower()
    include_kw = ['framework', 'sdk', 'agent-framework', 'multi-agent', 'autonomous-agent']
    exclude_kw = ['tutorial', 'demo', 'benchmark', 'paper', 'survey', 'list', 'awesome']
    if any(kw in desc for kw in exclude_kw):
        return False
    if any(kw in ' '.join(topics).lower() for kw in exclude_kw):
        return False
    # Include if any include_kw in desc or topics
    if any(kw in desc for kw in include_kw):
        return True
    if any(kw in ' '.join(topics).lower() for kw in include_kw):
        return True
    return False

def fetch_readme(full_name, branch):
    for name in ['README.md', 'README.rst', 'Readme.md', 'readme.md']:
        url = f'https://raw.githubusercontent.com/{full_name}/{branch}/{name}'
        try:
            with urllib.request.urlopen(url) as r:
                if r.status == 200:
                    return r.read().decode('utf-8')
        except Exception:
            continue
    return ''


def main():
    if len(sys.argv) < 2:
        print("Usage: github_pipeline.py <scraped_at>")
        sys.exit(1)
    scraped_at = sys.argv[1]
    data = json.load(sys.stdin)
    for repo in data:
        full_name = repo['full_name']
        if not in_scope(repo):
            continue
        readme = fetch_readme(full_name, repo['default_branch'])
        if not readme:
            continue
        name = full_name.split('/', 1)[1]
        front = ["---"]
        front.append(f'name: \"{name}\"')
        front.append(f'repo: \"{full_name}\"')
        front.append(f'url: \"{repo["html_url"]}\"')
        front.append(f'description: \"{repo["description"]}\"')
        front.append(f'stars: {repo["stargazers_count"]}')
        lang = repo.get('language') or ""
        front.append(f'language: \"{lang}\"')
        topics = repo.get('topics', [])
        topics_yaml = '[' + ', '.join(f'\"{t}\"' for t in topics) + ']'
        front.append(f'topics: {topics_yaml}')
        front.append(f'created_at: \"{repo["created_at"]}\"')
        front.append(f'pushed_at: \"{repo["pushed_at"]}\"')
        front.append('source: github')
        front.append(f'scraped_at: \"{scraped_at}\"')
        front.append("---")
        content = "\n".join(front) + "\n\n" + readme
        # Generate filename: replace slash with underscore
        fname = os.path.join('sources', f"github-{full_name.replace('/', '_')}.md")
        os.makedirs(os.path.dirname(fname), exist_ok=True)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Wrote {fname}')

if __name__ == '__main__':
    main()
