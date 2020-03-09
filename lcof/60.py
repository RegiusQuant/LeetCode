# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 上午10:17
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 60.py
# @Desc    : 说明

from typing import List


class Solution:

    def twoSum(self, n: int) -> List[float]:
        dp = [[0.] * (6 * n + 1) for _ in range(n)]
        for i in range(1, 7):
            dp[0][i] = 1 / 6

        for i in range(1, n):
            for j in range(i + 1, 6 * (i + 1) + 1):
                for k in range(1, 7):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k] / 6

        return dp[n - 1][n:]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(2))
