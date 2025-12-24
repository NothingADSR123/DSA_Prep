# 120. Triangle
# Medium
# Given a triangle array, return the minimum path sum from top to bottom
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
# Example 1:
# Input: trangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:
# Input: triangle = [[-10]]
# Output: -10

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dk how is it even a complex prob coz it was simple only understood onlu 
        # but ok O(n^2) there are other sols aswell like memo+recur but all same complexity
        dp=[0]*(len(triangle)+1)
        for row in triangle[::-1]:
            for j in range(len(row)):
                dp[j]=row[j] + min(dp[j],dp[j+1])
        return dp[0]
