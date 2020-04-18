# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 下午3:09
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

import bisect
from typing import List


class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        increase.insert(0, [0, 0, 0])
        n = len(increase)
        for i in range(1, n):
            for j in range(3):
                increase[i][j] += increase[i - 1][j]
        r = [x[0] for x in increase]
        c = [x[1] for x in increase]
        h = [x[2] for x in increase]
        # print(r, c, h)

        result = [0] * len(requirements)
        for i, x in enumerate(requirements):
            pr = bisect.bisect_left(r, x[0])
            pc = bisect.bisect_left(c, x[1])
            ph = bisect.bisect_left(h, x[2])
            t = max(pr, pc, ph)
            result[i] = t if t < n else -1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.getTriggerTime(
        [[2, 8, 4], [2, 5, 0], [10, 9, 8]],
        [[2, 11, 3], [15, 10, 7], [9, 17, 12], [8, 1, 14]]
    ))
    print(solution.getTriggerTime(
        [[0, 4, 5], [4, 8, 8], [8, 6, 1], [10, 10, 0]],
        [[12, 11, 16], [20, 2, 6], [9, 2, 6], [10, 18, 3], [8, 14, 9]]
    ))
    print(solution.getTriggerTime(
        [[2, 8, 4], [2, 5, 0], [10, 9, 8]],
        [[2, 8, 4], [4, 13, 3], [14, 22, 14], [8, 1, 14]]
    ))
    print(solution.getTriggerTime(
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[2, 8, 4], [4, 13, 3], [14, 22, 14], [8, 1, 14]]
    ))
    print(solution.getTriggerTime(
        [[1, 1, 1]],
        [[0, 0, 0]]
    ))
