# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 下午3:02
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        prev, curr = [1] + [0] * (n - 1), [0] * n
        for _ in range(k):
            for u, v in relation:
                curr[v] += prev[u]
            prev = curr.copy()
            curr = [0] * n
        return prev[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numWays(5, [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]], 3))
    print(solution.numWays(5, [[0, 2], [2, 1]], 2))
