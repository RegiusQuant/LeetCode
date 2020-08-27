# -*- coding: utf-8 -*-
# @Time       : 2020/08/27 22:19:24
# @Author     : RegiusQuant <315135833@qq.com>
# @Project    : LeetCode
# @File       : 0332.py
# @Description: 文件说明

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)
        for u, v in tickets:
            edges[u].append(v)
        for u in edges:
            heapq.heapify(edges[u])
        result = []

        def dfs(u):
            while edges[u]:
                v = heapq.heappop(edges[u])
                dfs(v)
            result.append(u)

        dfs('JFK')
        return result[::-1]
