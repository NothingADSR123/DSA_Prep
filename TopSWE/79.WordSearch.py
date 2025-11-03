# 79. Word Search
# Medium
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
# Example 1
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit=set()
        ROWS,COLS=len(board),len(board[0])
        def backtrack(r,c,index):
            if index==len(word):
                return True
            if r<0 or c<0 or r>=ROWS or c>=COLS or word[index]!=board[r][c] or (r,c) in visit:
                return False
            visit.add((r,c))
            res=(backtrack(r+1,c,index+1) or backtrack(r-1,c,index+1)
             or backtrack(r,c-1,index+1) or backtrack(r,c+1,index+1))
            visit.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0): return True
        return False