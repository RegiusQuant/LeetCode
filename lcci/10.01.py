# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 上午8:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 10.01.py
# @Desc    : 说明

from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        pa, pb, pc = m - 1, n - 1, m + n - 1
        while pa >= 0 or pb >= 0:
            if pb == -1 or (pa >= 0 and A[pa] > B[pb]):
                A[pc] = A[pa]
                pa -= 1
            else:
               A[pc] = B[pb]
               pb -= 1
            pc -= 1
