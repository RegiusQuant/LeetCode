# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 上午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0983.py
# @Desc    : 说明

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float('inf')] * n
        dp[0] = min(costs)

        for i in range(1, n):
            dp[i] = dp[i - 1] + min(costs)
            for j in range(i - 1, -1, -1):
                prevCost = 0 if j == 0 else dp[j - 1]
                if days[i] - days[j] < 7:
                    dp[i] = min(dp[i], prevCost + costs[1])
                if days[i] - days[j] < 30:
                    dp[i] = min(dp[i], prevCost + costs[2])
                else:
                    break
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.mincostTickets([1, 4, 6, 7, 8, 20], [7, 2, 15]))
