# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 上午10:07
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 66.py
# @Desc    : 说明

from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        left, right, result = [1] * n, [1] * n, [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * a[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * a[i + 1]
        for i in range(n):
            result[i] = left[i] * right[i]
        return result
