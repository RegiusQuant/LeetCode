# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 下午9:53
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0329.py
# @Desc    : 说明

from typing import List
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        @lru_cache(None)
        def dfs(cx, cy):
            best = 1
            for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
                if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] > matrix[cx][cy]:
                    best = max(best, dfs(nx, ny) + 1)
            return best

        result = 0
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                result = max(result, dfs(i, j))
        return result
