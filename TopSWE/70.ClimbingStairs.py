# 70. Climbing Stairs
# Easy
# You are climbing a staircase. It takes n steps to reach the top
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        # MORE OPTIMIZED O(n) and s-O(1)
        if n<=2: return n
        one,two=1,1
        for _ in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one


        # actual solution but can be optimized even more O(n) and S-O(n) without memoization
        # if n<=2: return n
        # dp=[0]*(n+1) #need this coz it makes sure index never goes out of bounds
        # dp[0]=1
        # dp[1]=1
        # for i in range(2,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]

        #WORKSSS recursion properly with memoization O(n)
        # memo={}
        # def help(i):
            
        #     if i <=2:return i
        #     if i in memo:
        #         return memo[i]
        #     memo[i]=help(i-2)+help(i-1)
        #     return memo[i]
        # return help(n)
        
        # DOesnt work coz ofc too much Time O(2^n)
        # if n<=2:
        #     return n
        # return self.climbStairs(n-1)+ self.climbStairs(n-2)
        