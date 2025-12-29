# 188. Best Time to Buy and Sell Stock IV
# Hard
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# Example 1:
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Same sol for buy and sell 3 works for this aswell idk why 
        dp=[[[0]*(k+1) for i in range(2)] for i in range(len(prices)+1)]
        for i in range(len(prices)-1,-1,-1):
            for buy in range(2):
                for cap in range(1,k+1):
                    if buy:
                        dp[i][buy][cap]= max(-prices[i]+ dp[i+1][0][cap],
                                                0 + dp[i+1][1][cap])
                    else:
                        dp[i][buy][cap]= max(prices[i] + dp[i+1][1][cap-1],
                                                0 + dp[i+1][0][cap])
        return dp[0][1][k]
        
        # memo={}
        # def dfs(i,buy,k):
        #     if k==0 or i==len(prices): return 0
        #     if (i,buy,k) in memo: return memo[(i,buy,k)]
        #     if buy:
        #         memo[(i,buy,k)]=max(-prices[i]+ dfs(i+1,False,k),
        #                                 0 + dfs(i+1,True,k))
        #     else:
        #         memo[(i,buy,k)]=max(prices[i]+ dfs(i+1,True,k-1),
        #                                 0 + dfs(i+1,False,k))
        #     return memo[(i,buy,k)]
        # return dfs(0,True,k)    