# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 下午10:14
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[1e10] * (n + 1) for _ in range(target + 1)] for _ in range(m)]

        if houses[0] > 0:
            dp[0][1][houses[0]] = 0
        else:
            for i in range(1, n + 1):
                dp[0][1][i] = cost[0][i - 1]

        for i in range(1, m):
            for j in range(1, target + 1):
                if houses[i] > 0:
                    for k in range(1, n + 1):
                        if houses[i] == k:
                            dp[i][j][houses[i]] = min(dp[i][j][houses[i]], dp[i - 1][j][k])
                        else:
                            dp[i][j][houses[i]] = min(dp[i][j][houses[i]], dp[i - 1][j - 1][k])
                else:
                    for k in range(1, n + 1):
                        for s in range(1, n + 1):
                            if k == s:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][s] + cost[i][k - 1])
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][s] + cost[i][k - 1])

        result = 1e10
        for i in range(1, n + 1):
            result = min(result, dp[m - 1][target][i])
        if result == 1e10:
            return -1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCost(
        [0, 0, 0, 0, 0],
        [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
        5, 2, 3
    ))

    print(solution.minCost(
        [0, 2, 1, 2, 0],
        [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
        5, 2, 3
    ))
