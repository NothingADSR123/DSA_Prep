# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Using separate rows and columns | T-O(m*n) S-O(m+n)
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        row_flags = [0] * rows
        col_flags = [0] * cols 
        # Step 1: Identify rows and columns to be zeroed
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_flags[i] = 1
                    col_flags[j] = 1
        # Step 2: Modify the matrix based on row_flags and col_flags
        for i in range(rows):
            for j in range(cols):
                if row_flags[i] == 1 or col_flags[j] == 1:
                    matrix[i][j] = 0


#OPTIMAL Using inside the matrix hi rows and columns | T-O(m*n) S-O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
        # Step 1: Use first row and column to mark zero positions
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Step 2: Zero out marked rows and columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    # Step 3: Handle first row and first column separately
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
