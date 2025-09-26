# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Brute Force But SEXILY

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
        # a=k%len(nums)
        # nums[:]=nums[-a:]+nums[:-a]
        # return nums
        
        
        
# Optimal Approach Using two pointers 

# k=k%len(nums)
        # l,r=0,len(nums)-1
        # while l<r:
        #     nums[l],nums[r]=nums[r],nums[l]
        #     l+=1
        #     r-=1
        # l,r=0,k-1
        # while l<r:
        #     nums[l],nums[r]=nums[r],nums[l]
        #     l+=1
        #     r-=1
        # l,r=k,len(nums)-1
        # while l<r:
        #     nums[l],nums[r]=nums[r],nums[l]
        #     l+=1
        #     r-=1
        # return nums
        