# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 下午9:26
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0007.py
# @Desc    : 说明

class Solution:
    def reverse(self, x: int) -> int:
        result, flag = 0, 1
        if x < 0:
            x = - x
            flag = -flag

        while x != 0:
            c = x % 10
            result = result * 10 + c
            x //= 10
        result *= flag
        return result if -2 ** 31 <= result < 2 ** 31 else 0
