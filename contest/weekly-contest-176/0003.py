# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 上午10:56
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        startDict = defaultdict(list)
        for event in events:
            startDict[event[0]].append(event[1])

        h, result = [], 0
        for i in range(1, int(1e5 + 1)):
            for end in startDict[i]:
                heapq.heappush(h, end)
            while len(h) > 0 and h[0] < i:
                heapq.heappop(h)
            if len(h) > 0:
                heapq.heappop(h)
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    events = [[1, 2], [2, 3], [3, 4]]
    print(solution.maxEvents(events))
    events = [[1, 2], [2, 3], [3, 4], [1, 2]]
    print(solution.maxEvents(events))
    events = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
    print(solution.maxEvents(events))
    events = [[1, 100000]]
    print(solution.maxEvents(events))
    events = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]
    print(solution.maxEvents(events))
    events = [[1, 2], [2, 3], [2, 3], [1, 3]]
    print(solution.maxEvents(events))
    events = [[1, 5], [1, 5], [1, 5], [2, 3], [2, 3]]
    print(solution.maxEvents(events))
