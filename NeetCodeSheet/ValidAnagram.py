# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true
# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# Next approach can be using a char array of 26 and checkin with that That will have O(n) and S-O(1)
# even better in space Both are optimal only

        d={}
        if len(s)!=len(t): return False
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        for i in range(len(t)):
            if t[i] in d and d[t[i]]>0:
                d[t[i]]-=1
            else:
                return False
        return True