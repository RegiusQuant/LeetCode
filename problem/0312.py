# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 上午10:03
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0312.py
# @Desc    : 说明

from typing import List
from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        @lru_cache(None)
        def solve(left, right):
            best = 0
            for i in range(left + 1, right):
                total = nums[left] * nums[i] * nums[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            return best
        return solve(0, n + 1)
