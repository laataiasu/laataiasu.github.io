import os
import re

def convert_tags_block(content):
    pattern = r"tags:\s*\n((?:\s*-\s*.+\n?)+)"

    def replacer(match):
        lines = match.group(1).strip().splitlines()
        tags = [line.strip().lstrip("-").strip() for line in lines]
        return f'tags: {tags}'.replace("'", '"') + '\n'

    return re.sub(pattern, replacer, content)

def process_md_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = convert_tags_block(content)

    if new_content != content:
        print(f"Updated: {file_path}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                process_md_file(full_path)

if __name__ == "__main__":
    import sys
    dir_to_scan = sys.argv[1] if len(sys.argv) > 1 else "."
    process_directory(dir_to_scan)
