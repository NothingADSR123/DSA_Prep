# Maximal Square
# Solved 
# You are given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# Example 1:
# Input: matrix = [
#     ["1","0","1","0","0"],
#     ["1","0","1","1","1"],
#     ["1","1","1","1","1"],
#     ["1","0","0","1","0"]
# ]
# Output: 4
# Example 2:
# Input: matrix = [
#     ["0","1"],
#     ["1","0"]
# ]
# Output: 1


from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[0]*len(matrix[0])for i in range(len(matrix))]
        res=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]= 1+ min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    res=max(res,dp[i][j])
        return res*res