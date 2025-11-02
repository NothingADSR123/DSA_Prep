# 51. N-Queens
# Hard
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:
# Input: n = 1
# Output: [["Q"]]
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols=set()
        posDig=set()#r+c
        negDig=set()#r-c
        board=[["."]*n for i in range(n)]
        res=[]
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board] )
                return
            for c in range(n):
                if c in cols or r+c in posDig or r-c in negDig:
                    continue
                cols.add(c)
                posDig.add(r+c)
                negDig.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)
                cols.remove(c)
                posDig.remove(r+c)
                negDig.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res