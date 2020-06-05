# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 下午9:21
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0064.py
# @Desc    : 说明

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                grid[i][j], t = float('inf'), grid[i][j]
                if i > 0:
                    grid[i][j] = min(grid[i][j], grid[i - 1][j] + t)
                if j > 0:
                    grid[i][j] = min(grid[i][j], grid[i][j - 1] + t)
        return grid[-1][-1]
