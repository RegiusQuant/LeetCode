# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 上午8:10
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0269.py
# @Desc    : 说明

from typing import List
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ''
        if len(words) == 1:
            return words[0]

        degs = {}
        for word in words:
            for c in word:
                degs[c] = 0

        edges = defaultdict(list)
        for i in range(1, len(words)):
            for j in range(min(len(words[i - 1]), len(words[i]))):
                if words[i - 1][j] != words[i][j]:
                    edges[words[i - 1][j]].append(words[i][j])
                    degs[words[i][j]] += 1
                    break
            else:
                if len(words[i - 1]) > len(words[i]):
                    return ''
        # print(degs)

        queue = deque()
        for u in degs.keys():
            if degs[u] == 0:
                queue.append(u)

        result = []
        while queue:
            u = queue.pop()
            result.append(u)
            for v in edges[u]:
                degs[v] -= 1
                if degs[v] == 0:
                    queue.append(v)

        if len(result) != len(degs):
            return ''
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.alienOrder(
    #     [
    #         "wrt",
    #         "wrf",
    #         "er",
    #         "ett",
    #         "rftt"
    #     ]
    # ))
    # print(solution.alienOrder(
    #     [
    #         "z",
    #         "x"
    #     ]
    # ))
    # print(solution.alienOrder(
    #     [
    #         "z",
    #         "x",
    #         "z"
    #     ]
    # ))
    print(solution.alienOrder(["za", "zb", "ca", "cb"]))
    print(solution.alienOrder(["abc", "ab"]))
    print(solution.alienOrder(["z", "z"]))
    print(solution.alienOrder(["wnlb"]))
