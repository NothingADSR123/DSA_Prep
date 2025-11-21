# 215. Kth Largest Element in an Array
# Medium
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
# There are approaches quickselect doesnt work due to TLE, heap works, sorting works 
# remember Heap and sorting

        #min Heap sol t-O(n log k)
        heap=[]
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]

        # Optimal kinda But it doesnt solve TLE so yeah my sol is best t-Avg O(n), worst O(n²)
        # k = len(nums) - k  # target index for k-th largest
        
        # def quickSelect(l, r):
        #     pivot = nums[r]
        #     p = l
        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[p], nums[i] = nums[i], nums[p]
        #             p += 1

        #     nums[p], nums[r] = nums[r], nums[p]

        #     if p > k:
        #         return quickSelect(l, p - 1)
        #     elif p < k:
        #         return quickSelect(p + 1, r)
        #     else:
        #         return nums[p]

        # return quickSelect(0, len(nums) - 1)
        
        
        # THis also solves but hm  O(n log n)
        # nums.sort()
        # return nums[-k]