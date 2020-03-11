# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 上午9:54
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 64.py
# @Desc    : 说明

class Solution:
    def sumNums(self, n: int) -> int:
        return n and n + self.sumNums(n - 1)
