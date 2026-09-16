#!/usr/bin/env python3
import argparse
import os
import re

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Separate YAML frontmatter from prose
    frontmatter_match = re.match(r"^(---\n.*?\n---\n)(.*)$", content, re.DOTALL)
    
    if not frontmatter_match:
        print(f"Skipped (no frontmatter found): {filepath}")
        return

    frontmatter_raw = frontmatter_match.group(1)
    prose = frontmatter_match.group(2)

    # 1. Calculate Word Count
    # Extracts all words, ignoring markdown headers/syntax symbols
    words = re.findall(r"\b\w+\b", prose)
    actual_word_count = len(words)

    # 2. Update Frontmatter word_count
    if "word_count:" in frontmatter_raw:
        updated_frontmatter = re.sub(
            r"word_count:\s*\d+",
            f"word_count: {actual_word_count}",
            frontmatter_raw
        )
    else:
        # Append before the closing delimiter if missing
        updated_frontmatter = frontmatter_raw.replace(
            "\n---",
            f"\nword_count: {actual_word_count}\n---"
        )

    new_content = updated_frontmatter + prose

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated word_count ({actual_word_count} words): {filepath}")
    else:
        print(f"Unchanged: {filepath}")

def main():
    for root, _, files in os.walk("exercises"):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()