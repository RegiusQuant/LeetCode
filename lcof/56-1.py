# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 上午9:05
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 56-1.py
# @Desc    : 说明

from typing import List
from functools import reduce


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        t = reduce(lambda x, y: x ^ y, nums)
        k, a, b = 1, 0, 0
        while t & k == 0:
            k <<= 1
        for x in nums:
            if k & x == 0:
                a ^= x
            else:
                b ^= x
        return [a, b]


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumbers([4, 1, 4, 6]))
    print(solution.singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))