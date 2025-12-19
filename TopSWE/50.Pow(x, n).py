# 50. Pow(x, n)
# Medium
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Good figuring out the optimal aswell Just couldnt write the exact code so chill
        # if n==0:
        #     return 1
        # if n <0:
        #     x=1/x
        #     n=-(n)
        # prev=x
        # while n>1:
        #     x=x*prev
        #     n-=1
        # return x

        # logn recursive
        def help(x,n):
            if x==0: return 0 
            if n==0: return 1
            res=help(x*x,n//2)
            return res*x if n%2==1 else res
        res=help(x,abs(n))
        return res if n>0 else 1/res