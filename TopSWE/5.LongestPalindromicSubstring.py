# 5. Longest Palindromic Substring
# Medium
# Given a string s, return the longest palindromic substring in s.
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:

        # question hi bakwas and complex hatt
        # COming inwards Top down app (This question is tricky understand the expl usig yt or chatgpt)
        # then we can understand the moving outwards thing and with odd and even lengths palindromes

# t-o(n^2) for all
        def expand(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        ans=""
        for i in range(len(s)):
            odd=expand(i,i)
            even=expand(i,i+1)
            ans=max(ans,odd,even,key=len)
        return ans

# And also dp solution idk its just a lil complex to understand but works since that is also bottom up 
# uses dp matrix thus space also s-O(n^2)

        # this memo recur sol doesnt work coz of recursion stack exploding memory 
        # so only sol that works is expanding outwards around the center
        # memo={}
        # ans=""
        # def dfs(i,j):
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if i>=j: return True
        #     memo[(i,j)]= True if s[i]==s[j] and dfs(i+1,j-1) else False
        #     return memo[(i,j)]
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         if dfs(i,j) and j-i+1>len(ans):
        #             ans=s[i:j+1]
        # return ans
