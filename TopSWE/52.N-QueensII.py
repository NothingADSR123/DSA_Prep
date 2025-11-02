# 52. N-Queens II
# Hard
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
# Example 1:
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:
# Input: n = 1
# Output: 1

class Solution:
    def totalNQueens(self, n: int) -> int:
        # A lil complicated we are usinhg sets for cols and diagonals refer yt
        cols=set()
        posD=set()#r+c
        negD=set()#r-c
        res=0
        def backtrack(r):
            if r==n:
                nonlocal res
                res+=1
                return
            for c in range(n):
                if c in cols or r+c in posD or r-c in negD:
                    continue
                cols.add(c)
                posD.add(r+c)
                negD.add(r-c)
                backtrack(r+1)
                cols.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
        backtrack(0)
        return res