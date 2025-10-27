# 17. Letter Combinations of a Phone Number
# Medium
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# Amapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
# Input: digits = "2"
# Output: ["a","b","c"]

from typing import List 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Ok ok not a hard problem but helps in understanding backtracking
        # DFS + UNDO
        if not digits: return []
        res=[]
        mappings= {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(index,letters):
            if len(letters)==len(digits):
                res.append("".join(letters))
                return
            for c in mappings[digits[index]]:
                letters.append(c)
                backtrack(index+1,letters)
                letters.pop()
        backtrack(0,[])
        return res