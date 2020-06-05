# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 下午9:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0070.py
# @Desc    : 说明

class Solution:
    def climbStairs(self, n: int) -> int:
        opt = [1] * 2
        for i in range(2, n + 1):
            opt[1], opt[0] = opt[1] + opt[0], opt[1]
        return opt[1]