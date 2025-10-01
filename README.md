# DSA_Preparation  

![Python](https://img.shields.io/badge/language-Python-blue)

A curated collection of Data Structures & Algorithms problems solved in Python.  

---

<!-- PROBLEM_TABLE_START -->
<!-- PROBLEM_TABLE_END -->






Each Python file is named as `<ID>.<ProblemName>.py`, so you can jump directly to it.

---

## 🧩 Example Code Snippet

Here’s how a typical solution looks (from `200.NumberOfIslands.py`):

```python
def numIslands(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1
                dfs(i, j)
    return count
```  

---

## 🤝 Contribution Guidelines

1. Fork the repo  
2. Clone locally  
3. Create a branch: `git checkout -b my-problem-folder`  
4. Add your solution in the correct topic folder, with naming `<ID>.<ProblemName>.py`  
5. Update the README’s problem index table (or run a script if automated)  
6. Submit a pull request — title as `Add <ProblemName> in <Topic>`  
7. I’ll review. Be sure your solution is clean, with comments if needed.

---

## 🛡 Credits

Thanks to LeetCode, algorithm teachers, and my code companions for inspiration.  
If you want to connect, drop a follow on github 😎

---

## 🌱 TODO / Roadmap

- Add **automated script** to refresh problem index table  
- Add **difficulty filters** / tags  
- Add **visual progress charts**  
- Support **Java / C++** solutions in parallel  

---

## 📝 Notes & Usage

- To run a solution: `python3 <topic>/<ID>.<ProblemName>.py`  
- Use this repo as a study reference — feel free to replicate the structure for your own solutions
