# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 下午7:01
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        data = [(e, s) for e, s in zip(efficiency, speed)]
        data.sort(reverse=True)

        h = []
        total, result = 0, 0
        for i in range(k):
            heapq.heappush(h, data[i][1])
            total += data[i][1]
            result = max(result, total * data[i][0])

        for i in range(k, n):
            total -= heapq.heappushpop(h, data[i][1])
            total += data[i][1]
            result = max(result, total * data[i][0])

        return result % int(1e9 + 7)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2))
    print(solution.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3))
    print(solution.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4))