# 64. Minimum Path Sum
# Medium
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# Example
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # lets see DP sol bottom up approach O(n*m)
        # 2D dp same t and s complexity though just better
        m,n=len(grid),len(grid[0])
        dp=[[float("inf")] * (n+1) for r in range(m+1)] 
        dp[m-1][n]=0
        for i in range(len(grid)-1,-1,-1):       
            for j in range(len(grid[0])-1,-1,-1):       
                dp[i][j]= grid[i][j] + min(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
        
        
        # recursion + memo O(n*m) coz it will be that for sure TOP down app
        # m,n=len(grid),len(grid[0])
        # memo={}
        # def dfs(i,j):
        #     if i==m-1 and j==n-1:
        #         return grid[i][j]
        #     if i>=m or j>=n:
        #         return float("inf")
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     memo[(i,j)]=grid[i][j] + min(dfs(i+1,j),dfs(i,j+1))
        #     return memo[(i,j)]
        # return dfs(0,0)