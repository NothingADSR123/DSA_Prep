# 201. Bitwise AND of Numbers Range
# Medium
# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
# Example 1:
# Input: left = 5, right = 7
# Output: 4
# Example 2:
# Input: left = 0, right = 0
# Output: 0
# Example 3:
# Input: left = 1, right = 2147483647
# Output: 0 

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Not optimal for larger inputs will give TLE O(n)
        # res=left
        # for i in range(left+1,right+1):
        #     res=res&i
        #     if res==0:
        #         return 0
        # return res

        # BEST KERNINGHANS O(logn)
        # while left<right:
        #     right= right & (right-1)
        # return right

        # BOTH ARE NICE APPROACHES THIS IS BIT SHIFTING FINDING MIDDLE GROUND O(logn)
        shift=0
        while left<right:
            left>>=1
            right>>=1
            shift+=1
        return right<<shift