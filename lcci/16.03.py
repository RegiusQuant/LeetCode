# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 下午4:07
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.03.py
# @Desc    : 说明

from typing import List


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        k1 = (end1[1] - start1[1]) / (end1[0] - start1[0]) if end1[0] != start1[0] else None
        b1 = start1[1] - k1 * start1[0] if k1 is not None else None
        k2 = (end2[1] - start2[1]) / (end2[0] - start2[0]) if end2[0] != start2[0] else None
        b2 = start2[1] - k2 * start2[0] if k2 is not None else None

        if k1 is None and k2 is None:
            if (
                    start1[0] == start2[0] and
                    min(start1[1], end1[1]) <= max(start2[1], end2[1]) and
                    min(start2[1], end2[1]) <= max(start1[1], end1[1])
            ):
                return max(min(start1, end1), min(start2, end2))

        elif k1 is None:
            y = k2 * start1[0] + b2
            if (start2[1] - y) * (end2[1] - y) <= 0:
                return [start1[0], y]

        elif k2 is None:
            y = k1 * start2[0] + b1
            if (start1[1] - y) * (end1[1] - y) <= 0:
                return [start2[0], y]

        else:
            if (
                    k1 == k2 and
                    b1 == b2 and
                    min(start1[1], end1[1]) <= max(start2[1], end2[1]) and
                    min(start2[1], end2[1]) <= max(start1[1], end1[1])
            ):
                return [max(min(start1[0], end1[0]), min(start2[0], end2[0])),
                        max(min(start1[1], end1[1]), min(start2[1], end2[1]))]
            elif k1 != k2:
                x = (b2 - b1) / (k1 - k2)
                y = k1 * x + b1
                if (start2[1] - y) * (end2[1] - y) <= 0 and (start1[1] - y) * (end1[1] - y) <= 0:
                    return [x, y]
        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.intersection([1, 1], [-1, 1], [1, 0], [-3, 2]))
