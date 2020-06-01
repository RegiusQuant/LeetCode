# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 上午10:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.result = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        s = set()
        edges = defaultdict(list)
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)
            s.add((u, v))
        self.dfs(-1, 0, edges, s)
        return self.result

    def dfs(self, p, u, edges, s):
        for v in edges[u]:
            if v != p:
                if (u, v) in s:
                    self.result += 1
                self.dfs(u, v, edges, s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
    solution = Solution()
    print(solution.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
    solution = Solution()
    print(solution.minReorder(5, [[1, 0], [2, 0]]))
