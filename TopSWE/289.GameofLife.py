# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.
# Given the current state of the board, update the board to reflect its next state.
# Note that you do not need to return anything.
# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        # m, n = len(board), len(board[0])  # Get the size of the board
        # copy_board = [[board[i][j] for j in range(n)] for i in range(m)]  # Copy the board
        # # Directions for 8 neighbors (top, bottom, left, right, diagonals)
        # directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        # for i in range(m):
        #     for j in range(n):
        #         # Count live neighbors
        #         live_neighbors = 0
        #         for dx, dy in directions:
        #             ni, nj = i + dx, j + dy
        #             if 0 <= ni < m and 0 <= nj < n and copy_board[ni][nj] == 1:
        #                 live_neighbors += 1

        #         # Apply rules:
        #         if board[i][j] == 1:  # If cell is alive
        #             if live_neighbors < 2 or live_neighbors > 3:
        #                 board[i][j] = 0  # Dies due to underpopulation or overpopulation
        #         else:  # If cell is dead
        #             if live_neighbors == 3:
        #                 board[i][j] = 1  # Becomes alive due to reproduction

        # Inplace with memory O(1)
        m, n = len(board), len(board[0])

        def count_live_neighbors(i, j):
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            return sum(1 for dx, dy in directions if 0 <= i + dx < m and 0 <= j + dy < n and abs(board[i + dx][j + dy]) == 1)

        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)

                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1  # Mark cell as dead (from 1 to 0)
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2  # Mark cell as alive (from 0 to 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1