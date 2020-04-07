# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 上午10:10
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.05.py
# @Desc    : 说明

class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A < B:
            A, B = B, A
        if B == 1:
            return A
        else:
            return A + self.multiply(A, B - 1)
