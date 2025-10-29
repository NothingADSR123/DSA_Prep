# 46. Permutations
# Medium
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # I have Written my own logic again 
        # Confuse maybe but think and do properly chill
        res=[]
        def backtrack(numbers):
            if len(numbers)==len(nums):
                res.append(numbers[:])
                return
            for i in range(len(nums)):
                if nums[i] in numbers:
                    continue
                numbers.append(nums[i])
                backtrack(numbers)
                numbers.pop()
        backtrack([])
        return res