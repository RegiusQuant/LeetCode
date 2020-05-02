# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 下午10:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List
from collections import defaultdict


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        hatToPerson = defaultdict(list)
        for i in range(len(hats)):
            for h in hats[i]:
                hatToPerson[h].append(i)

        n = len(hats)
        dp = [[0] * (1 << n) for i in range(42)]
        dp[0][0] = 1

        for i in range(41):
            for s in range(1 << n):
                dp[i + 1][s] = dp[i][s]

            for x in hatToPerson[i]:
                for s in range(1 << n):
                    if s & (1 << x) == 0:
                        dp[i + 1][s | (1 << x)] += dp[i][s]
                        dp[i + 1][s | (1 << x)] %= int(1e9 + 7)

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberWays([[3, 4], [4, 5], [5]]))
    print(solution.numberWays([[3, 5, 1], [3, 5]]))
    print(solution.numberWays([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))
    print(solution.numberWays([[1, 2, 3], [2, 3, 5, 6], [1, 3, 7, 9], [1, 8, 9], [2, 5, 7]]))

    print(solution.numberWays([[1, 3, 5, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 27, 34, 35, 38, 39, 40],
                               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25,
                                26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                               [3, 7, 10, 12, 13, 14, 15, 17, 21, 25, 29, 31, 35, 40],
                               [2, 3, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 24, 25, 28, 29, 32, 33, 34, 35,
                                36, 38], [6, 12, 17, 20, 22, 26, 28, 30, 31, 32, 34, 35],
                               [1, 4, 6, 7, 12, 13, 14, 15, 21, 22, 27, 28, 30, 31, 32, 35, 37, 38, 40],
                               [6, 12, 21, 25, 38],
                               [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                                27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40]]))
