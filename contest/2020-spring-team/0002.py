# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 下午4:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        left, right = 0, sum(time)
        result = right
        while left <= right:
            mid = (left + right) // 2
            if self.check(mid, time, m):
                right = mid - 1
                result = min(result, mid)
            else:
                left = mid + 1
        return result

    def check(self, t, time, m):
        count, temp, h = 1, 0, False
        mx = 0
        for x in time:
            mx = max(mx, x)
            if temp + x > t:
                if not h:
                    h = True
                    temp = temp - mx + x
                else:
                    count += 1
                    mx = x
                    if x > t:
                        temp = 0
                        h = True
                    else:
                        temp = x
                        h = False
            else:
                temp += x
        return count <= m


if __name__ == '__main__':
    solution = Solution()
    print(solution.minTime([1, 2, 3, 3], 2))
    print(solution.minTime([999, 999, 999], 4))
    print(solution.minTime([5, 1, 999], 2))
    print(solution.minTime([1000], 1))

    print(solution.minTime([1, 1, 999, 10, 1], 1))
    print(solution.minTime([1, 1, 1, 1, 1], 3))
    print(solution.minTime([1, 1, 10, 1, 10, 1], 2))
