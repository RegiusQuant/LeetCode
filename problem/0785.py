# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 下午9:34
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0785.py
# @Desc    : 说明

from typing import List


class Solution:
    def __init__(self):
        self.visit = {}
        self.result = True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        for i in range(len(graph)):
            if i not in self.visit:
                self.dfs(-1, i, graph)
        return self.result

    def dfs(self, p, u, edges):
        if u in self.visit:
            if self.visit[u] == p:
                self.result = False
            return
        self.visit[u] = -p
        for v in edges[u]:
            self.dfs(-p, v, edges)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
