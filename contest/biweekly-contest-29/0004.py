# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 下午9:56
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List
from collections import defaultdict, deque
from queue import PriorityQueue


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        edges = defaultdict(list)
        degs = [0] * n
        for u, v in dependencies:
            edges[u - 1].append(v - 1)
            degs[v - 1] += 1

        def findMaxDepth(u):
            depth, q = 0, deque([u])
            while q:
                for _ in range(len(q)):
                    u = q.popleft()
                    for v in edges[u]:
                        q.append(v)
                depth += 1
            return depth

        depth = [findMaxDepth(u) for u in range(n)]

        queue = PriorityQueue()
        for i in range(n):
            if degs[i] == 0:
                queue.put((-depth[i], i))

        result = 0
        while queue.qsize() != 0:
            temp = []
            for _ in range(min(k, queue.qsize())):
                u = queue.get()[1]
                for v in edges[u]:
                    degs[v] -= 1
                    if degs[v] == 0:
                        temp.append(v)
            for v in temp:
                queue.put((-depth[v], v))
            result += 1
        return result


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
