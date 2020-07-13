# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 下午9:16
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0174.py
# @Desc    : 说明

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[10 ** 9] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                temp = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(temp - dungeon[i][j], 1)
        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
