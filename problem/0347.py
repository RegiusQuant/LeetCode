# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 下午4:36
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0347.py
# @Desc    : 说明

import heapq
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter, h = Counter(nums), []
        for c, v in counter.items():
            if len(h) < k:
                heapq.heappush(h, (v, c))
            elif v > h[0][0]:
                heapq.heapreplace(h, (v, c))
        result = []
        while h:
            result.append(heapq.heappop(h)[1])
        return list(reversed(result))


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
