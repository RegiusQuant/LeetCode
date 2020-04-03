# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 上午10:00
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0289.py
# @Desc    : 说明

from typing import List
from copy import deepcopy


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        temp = deepcopy(board)

        for i in range(m):
            for j in range(n):
                count = 0
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and temp[x][y] == 1:
                        count += 1

                if temp[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 0
                if temp[i][j] == 0 and count == 3:
                    board[i][j] = 1
