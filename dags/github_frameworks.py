from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

PROJECT_ROOT = "/home/simon/documents/ai-researcher"
PYTHON = f"{PROJECT_ROOT}/.venv/bin/python3"
CLAUDE = "/home/simon/.local/bin/claude"
LOCAL_BIN = "/home/simon/.local/bin"

PROMPTS = {
    "popular": f"{PROJECT_ROOT}/prompts/github_frameworks_popular.md",
    "emerging": f"{PROJECT_ROOT}/prompts/github_frameworks_emerging.md",
}

SCHEDULES = {
    "popular": "@weekly",
    "emerging": "@daily",
}


def make_dag(mode: str) -> DAG:
    with DAG(
        dag_id=f"github_frameworks_{mode}",
        schedule=SCHEDULES[mode],
        start_date=datetime(2026, 6, 30),
        catchup=False,
        tags=["ai-researcher"],
    ) as dag:
        ingest = BashOperator(
            task_id="ingest",
            bash_command=f"{PROJECT_ROOT}/scripts/ingest_all.sh {PROMPTS[mode]}",
            cwd=PROJECT_ROOT,
            env={"PATH": f"{LOCAL_BIN}:/usr/local/bin:/usr/bin:/bin"},
            append_env=True,
        )

        update_hints = BashOperator(
            task_id="update_topic_hints",
            bash_command=f"{PYTHON} {PROJECT_ROOT}/scripts/update_topic_hints.py",
        )

        compile_wiki = BashOperator(
            task_id="compile_wiki",
            bash_command=f"{CLAUDE} -p '/llm-wiki-compiler:wiki-compile'",
            cwd=PROJECT_ROOT,
        )

        ingest >> update_hints >> compile_wiki

    return dag


dag_popular = make_dag("popular")
dag_emerging = make_dag("emerging")
