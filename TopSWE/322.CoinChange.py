# 322. Coin Change
# Medium
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2
# Input: cons = [2], amount = 3
# Output: -1
# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
# Also we cant do in a greedy approach taking only max value coz that wont give exact sol refer yt for example

        # Good only DP array wala same Time complexity and Bottom up approach
        dp=[float("inf")] * (amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i]=min(dp[i],1+dp[i-c])
        return dp[amount] if dp[amount]!=float("inf") else -1
        
        
        # Good solution memoization T-O(amount × n) Top Down
        # memo={}
        # def helper(curAmount):
        #     if curAmount==0:
        #         return 0
        #     if curAmount<0:
        #         return float("infinity")
        #     if curAmount in memo: return memo[curAmount]
        #     choice=float('infinity')
        #     for c in coins:
        #         choice=min(choice,1+helper(curAmount-c))
        #     memo[curAmount]=choice
        #     return choice
        # res= helper(amount)
        # if res != float("infinity"):
        #     return res
        # else: return -1