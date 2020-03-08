# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 下午8:38
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List
from collections import defaultdict, deque


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        tree = defaultdict(list)
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])
        prob, visit, = [0.] * (n + 1), [False] * (n + 1)
        dep, leaf = [0] * (n + 1), [False] * (n + 1)

        queue = deque()
        queue.append(1)
        prob[1], visit[1] = 1., True
        for k in range(t):
            temp = deque()
            while queue:
                u = queue.popleft()
                numNode = 0
                for v in tree[u]:
                    if not visit[v]:
                        numNode += 1

                if numNode == 0:
                    leaf[u] = True
                    continue

                for v in tree[u]:
                    if not visit[v]:
                        prob[v] = prob[u] / numNode
                        temp.append(v)
                        visit[v] = True
                        dep[v] = k + 1
            queue = temp

        if t > dep[target] and not leaf[target]:
            return 0.0
        return prob[target]


if __name__ == '__main__':
    solution = Solution()
    print(solution.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 20, 6))
    print(solution.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 1, 7))
    print(solution.frogPosition(8, [[2, 1], [3, 2], [4, 1], [5, 1], [6, 4], [7, 1], [8, 7]], 7, 7))
