# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 上午11:02
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 45.py
# @Desc    : 说明

from typing import List
from functools import cmp_to_key


def Comp(x, y):
    return int(str(x) + str(y)) - int(str(y) + str(x))


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = sorted(nums, key=cmp_to_key(Comp))
        return ''.join(map(str, nums))


if __name__ == '__main__':
    solution = Solution()
    print(solution.minNumber([10, 2]))
    print(solution.minNumber([3, 30, 34, 5, 9]))
