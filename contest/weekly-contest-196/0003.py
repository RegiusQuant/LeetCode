# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 下午2:15
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0] * n for _ in range(m)]

        result = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                dp[i][j] = dp[i][j - 1] + 1 if j > 0 else 1
                temp = dp[i][j]
                for k in range(i, -1, -1):
                    temp = min(temp, dp[k][j])
                    result += temp
        return result
