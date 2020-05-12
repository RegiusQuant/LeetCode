# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 下午8:30
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List
from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for e in edges:
            tree[e[0]].append(e[1])
        return self.helper(tree, hasApple, 0)

    def helper(self, tree, hasApple, u):
        if len(tree[u]) == 0:
            if hasApple[u]:
                return 2
            else:
                return 0

        temp = []
        for v in tree[u]:
            temp.append(self.helper(tree, hasApple, v))
        result = 0
        for i in range(len(temp)):
            if temp[i] != 0:
                result += temp[i]
        if u == 0:
            return result
        else:
            if result != 0 or hasApple[u]:
                return result + 2
            else:
                return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                           [False, False, True, False, True, True, False]))
    print(solution.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                           [False, False, True, False, False, True, False]))
    print(solution.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                           [False, False, False, False, False, False, False]))
    print(solution.minTime(4, [[0, 1], [1, 2], [0, 3]],
                           [True, True, True, True]))
