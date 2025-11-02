# 22. Generate Parentheses
# Medium
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]

from typing import List 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack,res=[],[]
        def backtrack(open,close):
            if open==n==close:
                res.append("".join(stack))
                return
            if open<n:
                stack.append("(")
                backtrack(open+1,close)
                stack.pop()
            if close<open:
                stack.append(")")
                backtrack(open,close+1)
                stack.pop()
        backtrack(0,0)
        return res