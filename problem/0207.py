# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 下午7:09
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0207.py
# @Desc    : 说明

from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deg, edges = [0] * numCourses, defaultdict(list)
        for u, v in prerequisites:
            edges[v].append(u)
            deg[u] += 1
        queue = [x for x in range(numCourses) if deg[x] == 0]
        while queue:
            u = queue.pop(0)
            for v in edges[u]:
                deg[v] -= 1
                if not deg[v]:
                    queue.append(v)
            edges[u] = []
        return not any(deg)


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(
        numCourses=2,
        prerequisites=[[1, 0]]
    ))
    print(solution.canFinish(
        numCourses=2,
        prerequisites=[[1, 0], [0, 1]]
    ))
    print(solution.canFinish(
        numCourses=3,
        prerequisites=[[1, 0], [2, 1]]
    ))
