#!/usr/bin/env python3
import os
import re

EXERCISES_DIR = "exercises"
INDEX_FILE = "INDEX.md"

def parse_frontmatter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Match content between triple dashes
    match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    frontmatter = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            frontmatter[key.strip()] = val.strip().strip('"')
    return frontmatter

def main():
    if not os.path.exists(EXERCISES_DIR):
        print(f"Directory '{EXERCISES_DIR}' not found.")
        return

    entries = []
    for filename in sorted(os.listdir(EXERCISES_DIR), reverse=True):
        if filename.endswith(".md"):
            filepath = os.path.join(EXERCISES_DIR, filename)
            meta = parse_frontmatter(filepath)
            if meta:
                entries.append((filename, meta))

    # Generate INDEX.md content
    lines = ["# Writing Sandbox Index\n", "| Date | Title | Summary | Status |\n| --- | --- | --- | --- |"]
    for filename, meta in entries:
        title = meta.get("title", filename)
        date = meta.get("date", "N/A")
        summary = meta.get("summary", "")
        status = meta.get("status", "raw")
        link = f"[{title}]({EXERCISES_DIR}/{filename})"
        lines.append(f"| {date} | {link} | {summary} | `{status}` |")

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Updated {INDEX_FILE} with {len(entries)} entries.")

if __name__ == "__main__":
    main()