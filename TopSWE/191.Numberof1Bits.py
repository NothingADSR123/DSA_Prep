# 191. Number of 1 Bits
# Easy
# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.
# Example 2:
# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.
# Example :
# Input: n = 2147483645
# Output: 30
# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        # # SOlved THIS is fastest time 4 minssss
        # res=0
        # while n >0:
        #     res+=1 if n%2==1 else 0
        #     n=n//2
        # return res

        # 1st trick approach this uses odd and even check normally and tells 
        # it still loops 32 times no matter what 
        # res=0
        # for _ in range(32):
        #     res= res+ (n&1)
        #     n=n>>1
        # return res

        # 2nd most optimal trick that works only for 1 bits not even 32 times
        # Kerninghan's approach
        res=0
        while n>0:
            n=n&(n-1)
            res+=1
        return res
            