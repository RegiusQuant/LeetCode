# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 下午12:13
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0210.py
# @Desc    : 说明

from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deg, edges = [0] * numCourses, defaultdict(list)
        for u, v in prerequisites:
            edges[v].append(u)
            deg[u] += 1

        queue = deque()
        for u in range(numCourses):
            if deg[u] == 0:
                queue.append(u)

        result = []
        while queue:
            u = queue.popleft()
            result.append(u)
            for v in edges[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    queue.append(v)
        return result if len(result) == numCourses else []


if __name__ == '__main__':
    solution = Solution()
    print(solution.findOrder(2, [[1, 0]]))
    print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
