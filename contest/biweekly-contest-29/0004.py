# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 下午9:56
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List
from collections import defaultdict, deque
from itertools import combinations
from functools import lru_cache


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        edges = defaultdict(list)
        for x, y in dependencies:
            edges[x - 1].append(y - 1)

        @lru_cache(None)
        def dfs(state):
            if state == (1 << n) - 1:
                return 0

            degs = [0] * n
            for u in range(n):
                if (1 << u) & state == 0:
                    for v in edges[u]:
                        degs[v] += 1
            # print(state)
            nodes = [u for u in range(n) if degs[u] == 0 and state & (1 << u) == 0]
            # print(nodes)

            if len(nodes) <= k:
                for u in nodes:
                    state |= (1 << u)
                return 1 + dfs(state)
            else:
                result = float('inf')
                for c in combinations(nodes, k):
                    newState = state
                    for u in c:
                        newState |= (1 << u)
                        result = min(result, 1 + dfs(newState))
                return result

        return dfs(0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minNumberOfSemesters(4, [[2, 1], [3, 1], [1, 4]], 2))
    print(solution.minNumberOfSemesters(5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2))
    print(solution.minNumberOfSemesters(11, [], 2))
    print(solution.minNumberOfSemesters(9,
                                        [[4, 8], [3, 6], [6, 8], [7, 6], [4, 2], [4, 1], [4, 7], [3, 7], [5, 2], [5, 9],
                                         [3, 4], [6, 9], [5, 7]], 2))
    print(solution.minNumberOfSemesters(8, [[2, 7], [1, 6], [2, 8], [8, 7], [6, 7], [5, 4], [1, 7], [1, 2], [1, 4],
                                            [2, 6]], 3))
