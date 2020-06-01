# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 下午1:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0240.py
# @Desc    : 说明

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        r, c = m - 1, 0
        while r >= 0 and c < n:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
        return False
