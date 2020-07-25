# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 下午9:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1025.py
# @Desc    : 说明

class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N + 1)
        for i in range(2, N + 1):
            for j in range(1, i):
                if i % j == 0 and dp[i - j] == False:
                    dp[i] = True
                    break
        return dp[-1]
