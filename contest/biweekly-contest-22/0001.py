# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return sum(all(abs(a1 - a2) > d for a2 in arr2) for a1 in arr1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))
    print(solution.findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))
    print(solution.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))
