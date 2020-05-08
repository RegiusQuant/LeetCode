# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 下午7:46
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0221.py
# @Desc    : 说明

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n, e = len(matrix), len(matrix[0]), 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    e = max(e, dp[i][j])

        return e * e
