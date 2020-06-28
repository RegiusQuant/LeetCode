# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 下午7:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue = deque()
        queue.append((points[0][0], points[0][1] - points[0][0]))
        result = float('-inf')
        for i in range(1, len(points)):
            while queue and points[i][0] - queue[0][0] > k:
                queue.popleft()
            if queue:
                result = max(result, queue[0][1] + points[i][0] + points[i][1])
            while queue and queue[-1][1] <= points[i][1] - points[i][0]:
                queue.pop()
            queue.append((points[i][0], points[i][1] - points[i][0]))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxValueOfEquation([[1, 3], [2, 0], [5, 10], [6, -10]], 1))
    print(solution.findMaxValueOfEquation([[0, 0], [3, 0], [9, 2]], 3))
