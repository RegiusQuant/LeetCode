# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 上午10:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List


class UnionFind:

    def __init__(self, n):
        self.root = [x for x in range(n)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.root[x] = y


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        for i in range(m):
            edges[i].append(i)
        edges.sort(key=lambda x: (x[2], x[0], x[1]))

        minCost = self.findMinTreeI(n, edges)

        result = [[], []]
        for i in range(m):
            if self.findMinTreeI(n, edges, i) > minCost:
                result[0].append(edges[i][-1])
            elif self.findMinTreeII(n, edges, i) == minCost:
                result[1].append(edges[i][-1])
        result[0].sort()
        result[1].sort()
        return result

    def findMinTreeI(self, n, edges, k=-1):
        uf = UnionFind(n)
        result, count = 0, 0
        for i, e in enumerate(edges):
            if i == k:
                continue
            x, y = uf.find(e[0]), uf.find(e[1])
            if x != y:
                result += e[2]
                count += 1
                if count == n - 1:
                    break
                uf.union(x, y)
        if count != n - 1:
            return float('inf')
        return result

    def findMinTreeII(self, n, edges, k):
        uf = UnionFind(n)
        result, count = 0, 0

        result += edges[k][2]
        count += 1
        uf.union(edges[k][0], edges[k][1])

        for i, e in enumerate(edges):
            if i == k:
                continue
            x, y = uf.find(e[0]), uf.find(e[1])
            if x != y:
                result += e[2]
                count += 1
                if count == n - 1:
                    break
                uf.union(x, y)
        if count != n - 1:
            return float('inf')
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findCriticalAndPseudoCriticalEdges(5, [[0, 1, 1], [1, 2, 1], [2, 3, 2],
                                                          [0, 3, 2], [0, 4, 3], [3, 4, 3],
                                                          [1, 4, 6]]))
    print(solution.findCriticalAndPseudoCriticalEdges(6, [[0, 1, 1], [1, 2, 1], [0, 2, 1],
                                                          [2, 3, 4], [3, 4, 2], [3, 5, 2],
                                                          [4, 5, 2]]))
