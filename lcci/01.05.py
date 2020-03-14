# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 下午2:54
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 01.05.py
# @Desc    : 说明

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        n, m = len(first), len(second)
        if abs(n - m) > 1:
            return False

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if first[i - 1] == second[j - 1]:
                    dp[i][j] = min(
                        dp[i - 1][j - 1],
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                    )
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + 1,
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                    )
        return dp[n][m] <= 1
