#!/usr/bin/env python3
"""
Sync .wiki-compiler.json topic_hints from sources/ filenames.

Extracts owner_repo from each github-<owner>_<repo>.md file and writes
the sorted list back into topic_hints. Run this before /wiki-compile so
the compiler has canonical framework names to anchor topic classification.
Using owner_repo guarantees uniqueness across repos with the same name.

Usage: python3 scripts/update_topic_hints.py
"""

import json
import os
import re

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)
SOURCES_DIR = os.path.join(REPO_ROOT, "sources")
CONFIG_PATH = os.path.join(REPO_ROOT, ".wiki-compiler.json")


def extract_slug(filename):
    m = re.match(r"github-(.+)\.md$", filename)
    return m.group(1).lower() if m else None


def main():
    names = sorted(filter(None, (
        extract_slug(f) for f in os.listdir(SOURCES_DIR)
    )))

    with open(CONFIG_PATH) as f:
        config = json.load(f)

    config["topic_hints"] = names

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)
        f.write("\n")

    print(f"Updated topic_hints: {len(names)} entries")


if __name__ == "__main__":
    main()
