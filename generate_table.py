import os
import re

README_FILE = "README.md"

PROBLEM_DIRS = {
    "TopSWE": {
        "title": "TopSWE Problems",
        "numbered": True
    },
    "NeetCodeSheet": {
        "title": "NeetCode Problems",
        "numbered": False
    }
}


def parse_numbered_filename(filename):
    match = re.match(r"(\d+)\.(.+)\.py", filename)
    if not match:
        return None, None
    return int(match.group(1)), match.group(2)


def generate_table(dir_name, numbered):
    rows = []

    for fname in os.listdir(dir_name):
        if not fname.endswith(".py"):
            continue

        rel_path = os.path.join(dir_name, fname)

        if numbered:
            pid, pname = parse_numbered_filename(fname)
            if pid is None:
                continue
            rows.append((pid, pname, rel_path))
        else:
            pname = fname.replace(".py", "")
            rows.append((pname, rel_path))

    if numbered:
        rows.sort(key=lambda x: x[0])
    else:
        rows.sort(key=lambda x: x[0].lower())

    md_rows = [
        "| # | Problem | Link |",
        "|---|---------|------|"
    ]

    if numbered:
        for pid, pname, link in rows:
            md_rows.append(f"| {pid} | {pname} | [Code]({link}) |")
        total = len(rows)
    else:
        for idx, (pname, link) in enumerate(rows, start=1):
            md_rows.append(f"| {idx} | {pname} | [Code]({link}) |")
        total = len(rows)

    return md_rows, total


def build_section(dir_name, meta):
    md_rows, total = generate_table(dir_name, meta["numbered"])
    return f"""<details>
<summary>{meta["title"]} (Total: {total})</summary>

{chr(10).join(md_rows)}

</details>
"""


def update_readme():
    with open(README_FILE, "r", encoding="utf-8") as f:
        readme = f.read()

    for dir_name, meta in PROBLEM_DIRS.items():
        section = build_section(dir_name, meta)
        start = f"<!-- {dir_name}_TABLE_START -->"
        end = f"<!-- {dir_name}_TABLE_END -->"

        if start in readme and end in readme:
            before = readme.split(start)[0]
            after = readme.split(end)[1]
            readme = f"{before}{start}\n{section}\n{end}{after}"
        else:
            readme += f"\n\n{start}\n{section}\n{end}"

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme)

    print("README updated.")


if __name__ == "__main__":
    update_readme()
