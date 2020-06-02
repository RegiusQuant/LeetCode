# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 上午10:11
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0263.py
# @Desc    : 说明

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num //= x
        return num == 1
