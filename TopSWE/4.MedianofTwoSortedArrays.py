# 4. Median of Two Sorted Arrays
# Hard
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# T
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums=nums1
        # nums.extend(nums2)
        # nums=sorted(nums)
        # total=len(nums)
        # if total%2==0:
        #     ans=nums[total//2]+nums[(total//2)-1]
        #     return ans/2
        # else:
        #     ans=nums[total//2]
        #     return ans
        # OPTIMAL HERE 
        A,B=nums1,nums2
        if len(B)<len(A):
            A,B=B,A
        total=len(A)+len(B)
        half=total//2
        l,r=0,len(A)-1
        while True:
            mid=(l+r)//2
            j=half-mid - 2 #dont know why
            Aleft=A[mid] if mid>=0 else float("-infinity")
            Aright=A[mid+1] if (mid+1)<len(A) else float("infinity")
            Bleft=B[j] if j>=0 else float("-infinity")
            Bright=B[j+1] if (j+1)<len(B) else float("infinity")

            if Aleft<=Bright and Aright>=Bleft:
                if total%2==0:
                    return (max(Aleft,Bleft) + min(Aright,Bright))/2
                else:
                    return min(Aright,Bright)
            elif Aleft>Bright:
                r=mid-1
            else:
                l=mid+1