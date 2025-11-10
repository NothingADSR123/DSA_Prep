# 33. Search in Rotated Sorted Array
# Medium
# There is an integer array nums sorted in ascending order (with distinct values)
# Prior to being passed to your function, nums is possibly left rotated at an unnown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # A lil trickuy due to the cases u have to handle but it is simple only
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            
            elif nums[l]<=nums[mid]: #it is basically left sorted part
                if target >nums[mid] or target < nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            else:                    #it is basivcallu right sortrf part
                if target <nums[mid] or target > nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
