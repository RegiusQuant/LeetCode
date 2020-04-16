# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 上午10:42
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.05.py
# @Desc    : 说明

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n:
            result += n // 5
            n //= 5
        return result
