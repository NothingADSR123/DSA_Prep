# 74. Search a 2D Matrix
# Medium
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

from typing import List 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        top,bot=0,rows-1 #THe catch to do binary search on rows first 
        while top<=bot:
            mid=(top+bot)//2
            if matrix[mid][0]>target:
                bot=mid-1
            elif matrix[mid][-1]<target:
                top=mid+1
            else:
                break
        if not top<=bot: return False #again catch to check if row have or not
        l,r=0,cols-1
        row=(top+bot)//2 #USing that row exactly
        while l<=r:
            m=(l+r)//2
            if matrix[row][m]==target:
                return True
            elif matrix[row][m]<target:
                l=m+1
            else:
                r=m-1
                
        return False