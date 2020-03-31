# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 上午10:21
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 05.01.py
# @Desc    : 说明

class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        for k in range(i, j + 1):
            if N & (1 << k):
                N -= 1 << k
        N += M << i
        return N
