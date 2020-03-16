# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 上午10:31
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 01.08.py
# @Desc    : 说明

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for r in rows:
            for j in range(n):
                matrix[r][j] = 0
        for c in cols:
            for i in range(m):
                matrix[i][c] = 0
