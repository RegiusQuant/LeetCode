# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 上午10:44
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 04.01.py
# @Desc    : 说明

from typing import List
from collections import defaultdict, deque


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        edges = defaultdict(list)
        for e in graph:
            edges[e[0]].append(e[1])

        queue = deque()
        queue.append(start)
        visit = set()
        visit.add(start)
        while queue:
            u = queue.popleft()
            if u == target:
                return True
            for v in edges[u]:
                if v not in visit:
                    queue.append(v)
                    visit.add(v)
        return False
