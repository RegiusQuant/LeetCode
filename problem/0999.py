# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 上午10:24
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0999.py
# @Desc    : 说明

from typing import List


class Solution:
    def __init__(self):
        self.result = 0

    def numRookCaptures(self, board: List[List[str]]) -> int:
        pos = (-1, -1)
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    pos = (i, j)
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = pos[0] + d[0], pos[1] + d[1]
            self.dfs(nx, ny, d, board)
        return self.result

    def dfs(self, cx, cy, d, board):
        if 0 <= cx < 8 and 0 <= cy < 8:
            if board[cx][cy] == 'B':
                return
            if board[cx][cy] == 'p':
                self.result += 1
                return
            nx, ny = cx + d[0], cy + d[1]
            self.dfs(nx, ny, d, board)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                                    [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
                                    [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                                    [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
                                   ))

    solution = Solution()
    print(solution.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                                    [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
                                    [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                                    [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
                                   ))

    solution = Solution()
    print(solution.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                                    [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
                                    [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
                                    [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
                                   ))
