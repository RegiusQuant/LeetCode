# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 上午10:41
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 10.09.py
# @Desc    : 说明

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            if target < matrix[r][c]:
                c -= 1
            else:
                r += 1
        return False
