# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
# Inut: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashset=set(nums)
        longest=0
        for i in hashset:
            if (i-1) not in hashset:
                count=0
                while (i+count) in hashset:
                    count+=1
                longest=max(longest,count)
        return longest


        