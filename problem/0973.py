# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 上午8:32
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0973.py
# @Desc    : 说明

import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2

        def helper(start, end, k):
            if start >= end:
                return
            p1, p2, p3 = start, end, random.randint(start, end)
            temp = points[p3]

            points[p1], points[p3] = points[p3], points[p1]
            pivot = dist(p1)

            while p1 < p2:
                while p1 < p2 and dist(p2) >= pivot:
                    p2 -= 1
                points[p1] = points[p2]
                while p1 < p2 and dist(p1) <= pivot:
                    p1 += 1
                points[p2] = points[p1]
            points[p1] = temp
            if k <= p1 - start + 1:
                helper(start, p1, k)
            else:
                helper(p1 + 1, end, k - (p1 - start + 1))

        helper(0, len(points) - 1, K)
        return points[:K]


if __name__ == '__main__':
    solution = Solution()
    print(solution.kClosest([[1, 3], [-2, 2]], 1))
    print(solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
    print(solution.kClosest([[0, 1], [1, 0]], 2))
    print(solution.kClosest([[-2, -6], [-7, -2], [-9, 6], [10, 3], [-8, 1], [2, 8]], 5))
