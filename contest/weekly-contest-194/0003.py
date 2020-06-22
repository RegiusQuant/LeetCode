# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 上午10:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List
from collections import defaultdict


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        state = defaultdict(list)
        result = [-1] * len(rains)
        for i, x in enumerate(rains):
            if x > 0 and len(state[x]) > 0:
                for j in range(len(state[0])):
                    if state[0][j] > state[x][-1]:
                        result[state[0][j]] = x
                        state[0].pop(j)
                        break
                else:
                    return []
            state[x].append(i)
        for p in state[0]:
            result[p] = 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.avoidFlood([1, 2, 3, 4]))
    print(solution.avoidFlood([1, 2, 0, 0, 2, 1]))
    print(solution.avoidFlood([1, 2, 0, 1, 2]))
    print(solution.avoidFlood([69, 0, 0, 0, 69]))
    print(solution.avoidFlood([10, 20, 20]))
