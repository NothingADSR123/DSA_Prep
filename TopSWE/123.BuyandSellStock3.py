# 123. Best Time to Buy and Sell Stock III
# Hard
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# Example 1:
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:
# Input: prces = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
# there is an even more opt sol with O(n) but it is non intuitive so lets not 

# Multi dp so In this there is 3D dp coz three factors- i,buy,cap 
        dp=[[[0]* 3 for u in range(2)] for _ in range(len(prices)+1)]
        for i in range(len(prices)-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):      # This range 1,3 is imp idk why because If you allow 
                                            # cap = 0 here, then: # cap - 1 = -1
                    if buy==1:
                        dp[i][buy][cap]= max(-prices[i]+dp[i+1][0][cap],
                                                0 + dp[i+1][1][cap])
                    else:
                        dp[i][buy][cap]= max(prices[i]+ dp[i+1][1][cap-1],
                                                0 + dp[i+1][0][cap])
        return dp[0][1][2]
                        


        # memo+recus sol too much time and memory used not very optimal
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
        # return dfs(0,True,2)