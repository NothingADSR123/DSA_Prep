# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count={}
        for i in s1: 
            count[i]=1+count.get(i,0)
        l=0
        count2={}

        for r in range(len(s2)):
            count2[s2[r]]=1+count2.get(s2[r],0)

            while r-l+1 > len(s1):
                count2[s2[l]]-=1
                if count2[s2[l]]==0:
                    del count2[s2[l]]

                l+=1

            if count==count2:
                return True
        return False    