# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 下午6:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0322.py
# @Desc    : 说明

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            dp[i] = float('inf')
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] < float('inf') else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))
    print(solution.coinChange([2], 3))
