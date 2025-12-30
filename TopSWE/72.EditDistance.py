# 72. Edit Distance
# Medium
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character
# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # memo+recur
        # m,n=len(word1),len(word2)
        # memo={}
        # def dfs(i,j):
        #     if i==m:
        #         return n-j
        #     if j==n:
        #         return m-i
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if word1[i]==word2[j]:
        #         ans= dfs(i+1,j+1)
        #     else:
        #         ans= 1 + min(dfs(i+1,j),dfs(i,j+1),dfs(i+1,j+1))
        #     memo[(i,j)]=ans
        #     return ans
        # return dfs(0,0)

        # DP approach 
        dp=[[float("inf")]*(len(word2)+1) for i in range(len(word1)+1)]
        dp[len(word1)][len(word2)]=0
        for j in range(len(word2)+1):
            dp[len(word1)][j]=len(word2)-j
        for i in range(len(word1)+1):
            dp[i][len(word2)]=len(word1)-i
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]= 1 + min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
        return dp[0][0]