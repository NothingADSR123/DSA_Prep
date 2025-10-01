import os
import re

BASE_DIR = "TopSWE"        # folder with all problems
README_FILE = "README.md"  # main README to update

def parse_filename(filename):
    match = re.match(r"(\d+)\.(.+)\.py", filename)
    if not match:
        return None, None
    return int(match.group(1)), match.group(2)

def generate_table(base_dir):
    rows = []
    for fname in os.listdir(base_dir):
        if fname.endswith(".py"):
            pid, pname = parse_filename(fname)
            if pid is None:
                continue
            rel_path = os.path.join(base_dir, fname)
            rows.append((pid, pname, rel_path))
    rows.sort(key=lambda x: x[0])
    md_rows = ["| # | Problem | Link / File |",
               "|---|---------|-------------|"]
    for pid, pname, link in rows:
        md_rows.append(f"| {pid} | {pname} | [Code]({link}) |")
    return md_rows, len(rows)

def update_readme():
    md_rows, total = generate_table(BASE_DIR)
    table_content = "<details>\n<summary>📊 Problems Solved (Total: {})</summary>\n\n{}\n\n</details>".format(
        total, "\n".join(md_rows)
    )

    # Read README
    with open(README_FILE, "r", encoding="utf-8") as f:
        readme_text = f.read()

    # Replace existing table between markers
    start_marker = "<!-- PROBLEM_TABLE_START -->"
    end_marker = "<!-- PROBLEM_TABLE_END -->"

    if start_marker in readme_text and end_marker in readme_text:
        prefix = readme_text.split(start_marker)[0]
        suffix = readme_text.split(end_marker)[1]
        new_readme = f"{prefix}{start_marker}\n{table_content}\n{end_marker}{suffix}"
    else:
        # If markers not found, append at end
        new_readme = readme_text + "\n\n" + start_marker + "\n" + table_content + "\n" + end_marker

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_readme)
    print(f"README updated with {total} problems.")

if __name__ == "__main__":
    update_readme()
