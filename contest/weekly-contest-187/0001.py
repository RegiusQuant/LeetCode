# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 上午10:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List
from collections import defaultdict


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        edge = defaultdict(list)
        s = set()
        for ca, cb in paths:
            s.add(ca)
            s.add(cb)
            edge[ca].append(cb)

        for c in s:
            if len(edge[c]) == 0:
                return c
        return None


if __name__ == '__main__':
    solution = Solution()
    print(solution.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
    print(solution.destCity([["B", "C"], ["D", "B"], ["C", "A"]]))
    print(solution.destCity([["A", "Z"]]))
