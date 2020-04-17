# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 上午11:05
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.07.py
# @Desc    : 说明

class Solution:
    def maximum(self, a: int, b: int) -> int:
        k = (a - b) & (2 ** 33)
        k >>= 33
        return k * b + a * (k ^ 1)
