# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 上午12:51
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0309.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 1:
            return 0

        dp = [[0] * 3 for _ in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]

        return max(dp[-1][0], dp[-1][2])


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([1, 2, 3, 0, 2]))
