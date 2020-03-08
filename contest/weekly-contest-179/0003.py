# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 下午8:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List
from collections import defaultdict


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        edges = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                edges[manager[i]].append(i)
        return self.dfs(edges, informTime, headID, 0)

    def dfs(self, edges, informTime, u, t):
        if len(edges[u]) == 0:
            return t
        result = 0
        for v in edges[u]:
            result = max(result, self.dfs(edges, informTime, v, t + informTime[u]))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]))
    print(solution.numOfMinutes(7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]))
