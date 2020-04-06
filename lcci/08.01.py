# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 上午10:48
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.01.py
# @Desc    : 说明

class Solution:
    def waysToStep(self, n: int) -> int:
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        for i in range(3, n + 1):
            dp[0], dp[1], dp[2] = dp[1], dp[2], sum(dp) % int(1e9 + 7)
        return dp[-1]
