# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 上午10:15
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 40.py
# @Desc    : 说明

import heapq
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        h, result = [], []
        for x in arr:
            heapq.heappush(h, -x)
            if len(h) > k:
                heapq.heappop(h)
        while len(h) > 0:
            result.append(-heapq.heappop(h))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.getLeastNumbers([0, 1, 2, 1], 1))
