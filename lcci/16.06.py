# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 上午10:53
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.06.py
# @Desc    : 说明

from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        p1, p2 = 0, 0
        result = float('inf')
        while p1 < len(a) and p2 < len(b):
            result = min(result, abs(a[p1] - b[p2]))
            if a[p1] < b[p2]:
                p1 += 1
            else:
                p2 += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestDifference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))
