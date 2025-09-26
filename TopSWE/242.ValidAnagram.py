# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# # Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sM,tM={},{}
        for i in range(len(s)):
            sM[s[i]]=sM.get(s[i],0)+1
            tM[t[i]]=tM.get(t[i],0)+1

        if sM==tM:
            return True 
        else :
            return False
