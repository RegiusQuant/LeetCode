# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 下午9:07
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1192.py
# @Desc    : 说明

from typing import List
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edges = defaultdict(list)
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)

        conns = set(map(tuple, (map(sorted, connections))))
        rank = [-1] * n

        def dfs(prev, node, depth):
            if rank[node] >= 0:
                return rank[node]

            rank[node] = depth
            minDepth = n
            for v in edges[node]:
                if v == prev:
                    continue
                backDepth = dfs(node, v, depth + 1)
                if backDepth <= depth:
                    conns.discard(tuple(sorted((node, v))))
                minDepth = min(minDepth, backDepth)
            return minDepth

        dfs(-1, 0, 0)
        return list(conns)


if __name__ == '__main__':
    solution = Solution()
    print(solution.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
