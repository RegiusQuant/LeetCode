# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 上午10:46
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List
from functools import lru_cache


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])

        apple = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                apple[i][j] = 1 if pizza[i][j] == 'A' else 0
                if i == m - 1 and j == n - 1:
                    continue
                elif i == m - 1:
                    apple[i][j] += apple[i][j + 1]
                elif j == n - 1:
                    apple[i][j] += apple[i + 1][j]
                else:
                    apple[i][j] += apple[i + 1][j] + apple[i][j + 1] - apple[i + 1][j + 1]

        @lru_cache(None)
        def helper(x, y, z):
            nums = apple[x][y]
            if nums < z:
                return 0
            if z == 1:
                return 1

            result = 0
            for i in range(x + 1, m):
                if apple[i][y] < nums:
                    result += helper(i, y, z - 1)
            for j in range(y + 1, n):
                if apple[x][j] < nums:
                    result += helper(x, j, z - 1)
            return result % (10 ** 9 + 7)

        return helper(0, 0, k)


if __name__ == '__main__':
    solution = Solution()
    print(solution.ways(["A..", "AAA", "..."], 3))
    print(solution.ways(["A..", "AA.", "..."], 3))
    print(solution.ways(["A..", "A..", "..."], 1))
