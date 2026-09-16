# Writing Sandbox

A modular, plain-text creative writing sandbox built with Markdown, YAML frontmatter, and Python automation. This repository serves as an exercise gym for honing core prose skills before integrating snippets into a larger world-building project.

---

## 📁 Repository Structure

```text
writing-sandbox/
├── .github/
│   └── workflows/          # GitHub Actions CI checks
├── exercises/              # Practice snippets & micro-fiction tests
├── world-building/         # Modular assets (locations, factions, artifacts)
├── scripts/                # Utility CLI automation tools
│   ├── new_exercise.py     # Generator for new exercise files
│   ├── format_prose.py     # Word count calculator & frontmatter updater
│   └── build_index.py      # Automated INDEX.md generator
├── TAGS.md                 # Master tag taxonomy registry
├── INDEX.md                # Generated catalog of all writing entries
└── README.md               # Repository documentation
```

## 🛠️ CLI Tooling & Automation
All local scripts are located in the scripts/ directory and run using Python 3:

### 1. Create a New Exercise
Generate a pre-formatted Markdown file with YAML frontmatter in `exercises/`:

    ```sh
    python3 scripts/new_exercise.py "Story Title" -s "A 1-line summary." -t skill/sensory tone/anxiety
    ```

### 2. Update Word Counts
Scan all Markdown files in `exercises/`, calculate prose word count, and update the YAML word_count field:

```sh
python3 scripts/format_prose.py exercises
```

### 3. Rebuild Index
Scan all entries and regenerate `INDEX.md` with a clean summary table:

```sh
python3 scripts/build_index.py
```

## 🏷️ Frontmatter & Tag Taxonomy
Every snippet file uses standardized YAML frontmatter at the top of the file:

```yaml
---
title: "The Old Lighthouse Engine"
date: 2026-09-16
summary: "A scene focusing on metallic smells during a coastal storm."
word_count: 182
status: raw
tags:
  - skill/sensory
  - tone/anxiety
  - asset/location
---
```

### Status Lifecycle

- `raw`: Initial unedited draft freshly written during an exercise.
- `polished`: Edited for grammar, word count constraints, and stylistic flow.
- `plugged`: Integrated into a larger modular world-building asset.
- `archived`: Retired draft or reference material.

> Refer to `TAGS.md` for the complete list of accepted tags.

## 🚀 Workflow Guide

1. Generate: Run `python3 scripts/new_exercise.py "Title" -s "Summary" -t tag1 tag2`.

2. Draft: Write your prose inside the newly created Markdown file in `exercises/`.

3. Commit: Save and commit using Git. The local pre-commit hook automatically updates word counts and refreshes `INDEX.md`:

    ```sh
    git add .
    git commit -m "Add new practice exercise"
    git push
    ```