# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午1:35
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        degs = [0] * numCourses
        for v, u in prerequisites:
            edges[u].append(v)
            degs[v] += 1

        queue = deque()
        visit = [False] * numCourses
        for i in range(numCourses):
            if degs[i] == 0:
                queue.append(i)
                visit[i] = True

        while queue:
            u = queue.popleft()
            for v in edges[u]:
                degs[v] -= 1
                if degs[v] == 0:
                    queue.append(v)
                    visit[v] = True
        return sum(visit) == numCourses


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))
    print(solution.canFinish(2, [[1, 0], [0, 1]]))
