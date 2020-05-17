# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 下午12:46
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

import math
from typing import List


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:

        def distance(x1, y1, x2, y2):
            return math.sqrt(float((x1 - x2) ** 2) + float((y1 - y2) ** 2))

        def center(x1, y1, x2, y2, r):
            mx = (x1 + x2) / 2.0
            my = (y1 + y2) / 2.0
            angle = math.atan2(float(y2 - y1), float(x2 - x1))
            d = math.sqrt(r ** 2 - distance(x1, y1, mx, my) ** 2)
            cx = mx + d * math.sin(angle)
            cy = my - d * math.cos(angle)
            return cx, cy

        result = 1
        r = float(r)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if distance(points[i][0], points[i][1], points[j][0], points[j][1]) > r * 2:
                    continue
                cx, cy = center(points[i][0], points[i][1], points[j][0], points[j][1], r)
                count = 0
                for k in range(len(points)):
                    if distance(cx, cy, points[k][0], points[k][1]) < r + 1e-8:
                        count += 1
                result = max(result, count)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numPoints([[-2, 0], [2, 0], [0, 2], [0, -2]], 2))
    print(solution.numPoints([[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], 5))
    print(solution.numPoints([[-2, 0], [2, 0], [0, 2], [0, -2]], 1))
    print(solution.numPoints([[1, 2], [3, 5], [1, -1], [2, 3], [4, 1], [1, 3]], 2))
