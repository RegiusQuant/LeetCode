# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 上午12:18
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0130.py
# @Desc    : 说明

from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.mark = []

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        self.mark = [[0] * n for _ in range(m)]
        for j in range(n):
            if board[0][j] == 'O':
                self.fill(0, j, board)
            if board[m - 1][j] == 'O':
                self.fill(m - 1, j, board)
        for i in range(m):
            if board[i][0] == 'O':
                self.fill(i, 0, board)
            if board[i][n - 1] == 'O':
                self.fill(i, n - 1, board)

        for i in range(m):
            for j in range(n):
                if not self.mark[i][j]:
                    board[i][j] = 'X'

    def fill(self, x, y, board):
        m, n = len(board), len(board[0])
        queue = deque([(x, y)])
        self.mark[x][y] = 1
        while queue:
            cx, cy = queue.popleft()
            for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                if 0 <= nx < m and 0 <= ny < n and not self.mark[nx][ny] and board[nx][ny] == 'O':
                    self.mark[nx][ny] = 1
                    queue.append((nx, ny))


if __name__ == '__main__':
    solution = Solution()
    solution.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
