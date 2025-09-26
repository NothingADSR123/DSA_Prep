# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
# Eample 1:
# Iput: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Explanation:
# The bijection can be established as:
# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:
# Input: attern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3
# Input: pttern = "aaaa", s = "dog cat cat dog"
# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=s.split(" ")
        ps={}
        sp={}
        if len(pattern)!=len(l):
            return False
        for c,w in zip(pattern,l):
            if c in ps and ps[c]!=w:
                return False
            elif w in sp and sp[w]!=c:
                return False
            ps[c]=w
            sp[w]=c
        return True
