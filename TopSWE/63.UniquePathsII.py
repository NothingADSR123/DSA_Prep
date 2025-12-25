# 63. Unique Paths II
# Medium
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Anobsacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return te number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109
# Example 1
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1


from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
# Simple only nothing hard simply understand and do 

        # bottom up 2D dp
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1]==1:
            return 0

        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    if i>0:
                        dp[i][j]=dp[i][j]+ dp[i-1][j]
                    if j>0:
                        dp[i][j]=dp[i][j]+dp[i][j-1]
        return dp[m-1][n-1]


        # recus+memo top down app
        # m,n=len(obstacleGrid),len(obstacleGrid[0])
        # if obstacleGrid[m-1][n-1]==1: return 0
        # memo={}
        # def dfs(i,j):
        #     if i==m-1 and j==n-1 :
        #         return 1
        #     if i>=m or j>=n or obstacleGrid[i][j]==1:
        #         return 0
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     memo[(i,j)]=dfs(i+1,j) + dfs(i,j+1)
        #     return memo[(i,j)]
        # return dfs(0,0)