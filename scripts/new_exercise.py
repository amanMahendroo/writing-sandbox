#!/usr/bin/env python3
import argparse
import datetime
import os
import re

TEMPLATE = """---
title: "{title}"
date: {date}
summary: "{summary}"
word_count: 0
status: raw
tags:
{tags}
---

# {title}

Write your prose here...
"""

def slugify(text):
    """Converts a title like 'The Old Harbor' into 'the-old-harbor'."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    return re.sub(r'[\s_]+', '-', text).strip('-')

def main():
    parser = argparse.ArgumentParser(description="Create a new micro-fiction exercise file.")
    parser.add_argument("title", help="Title of the exercise")
    parser.add_argument("-s", "--summary", default="", help="1-line summary of the piece")
    parser.add_argument("-t", "--tags", nargs="*", default=[], help="List of tags (e.g. -t skill/sensory tone/anxiety)")
    parser.add_argument("-o", "--output-dir", default="exercises", help="Target directory (default: exercises)")

    args = parser.parse_args()

    # Format Date and File Name
    today_str = datetime.date.today().isoformat()
    slug_title = slugify(args.title)
    filename = f"{today_str}-{slug_title}.md"
    filepath = os.path.join(args.output_dir, filename)

    # Format Tags for YAML
    if args.tags:
        formatted_tags = "\n".join([f"  - {tag}" for tag in args.tags])
    else:
        formatted_tags = "  # - ADD_TAGS_HERE"

    # Fill Template
    content = TEMPLATE.format(
        title=args.title,
        date=today_str,
        summary=args.summary,
        tags=formatted_tags
    )

    # Ensure output directory exists and write file
    os.makedirs(args.output_dir, exist_ok=True)
    
    if os.path.exists(filepath):
        print(f"Error: File '{filepath}' already exists.")
        return

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created new exercise: {filepath}")

if __name__ == "__main__":
    main()