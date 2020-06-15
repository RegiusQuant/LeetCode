# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 下午10:00
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()

        n = len(houses)
        rec = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                m = (i + j) // 2
                for x in range(i, j + 1):
                    rec[i][j] += abs(houses[x] - houses[m])
        print(rec)

        dp = [[10 ** 7] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = rec[0][i]
        for i in range(n):
            for j in range(2, min(i + 1, k) + 1):
                for x in range(j - 1, i + 1):
                    dp[i][j] = min(dp[i][j], dp[x - 1][j - 1] + rec[x][i])
        return dp[n - 1][k]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance([1, 4, 8, 10, 20], 3))
    print(solution.minDistance([2, 3, 5, 12, 18], 2))
    print(solution.minDistance([7, 4, 6, 1], 1))
    print(solution.minDistance([3, 6, 14, 10], 4))
    print(solution.minDistance([1, 8, 12, 10, 3], 3))
    print(solution.minDistance([1, 3, 12, 7, 6], 2))

    print(solution.minDistance([2, 3, 5, 12, 18], 2))