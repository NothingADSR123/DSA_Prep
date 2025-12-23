# 300. Longest Increasing Subsequence
# Medium
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # BEST O(nlogn) binary search watch TUF ka yt very big brain moves
        # not exact LIS but just keeping the length of LIS
        tail=[]
        for i in range(len(nums)):
            left,right=0,len(tail)-1
            pos=len(tail)
            while left<=right:
                mid=(left+right)//2
                if tail[mid]>=nums[i]:
                    pos=mid
                    right=mid-1
                else:
                    left=mid+1
            if pos==len(tail):
                tail.append(nums[i])
            else:
                tail[pos]=nums[i]
        return len(tail)


        # T-O(n^2) nice but can be better 
        # dp=[1]*len(nums)
        # for i in range(len(nums)-1,-1,-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]<nums[j]:
        #             dp[i]=max(dp[i],1+dp[j])
        # return max(dp)