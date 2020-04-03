# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 上午10:26
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 05.06.py
# @Desc    : 说明

class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        t, c = (A ^ B) & 0xffffffff, 0
        while t:
            t = t & (t - 1)
            c += 1
        return c
