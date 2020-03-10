# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 上午10:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 62.py
# @Desc    : 说明

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        result = 0
        for i in range(2, n + 1):
            result = (result + m) % i
        return result
