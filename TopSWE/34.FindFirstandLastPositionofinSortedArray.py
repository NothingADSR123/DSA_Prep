# 34. Find First and Last Position of Element in Sorted Array
# Medium
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.xample 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

from typing import List 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.helperBinSearch(nums,target,True)
        right=self.helperBinSearch(nums,target,False)
        return [left,right]
    def helperBinSearch(self,nums,target,leftBias):
        l,r=0,len(nums)-1
        index=-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                index=m
                if leftBias:
                    r=m-1
                else:
                    l=m+1
        return index


