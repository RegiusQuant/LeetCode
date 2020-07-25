# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 下午7:42
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0410.py
# @Desc    : 说明

from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right, result = max(nums), sum(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if self.check(mid, m, nums):
                right = mid - 1
                result = mid
            else:
                left = mid + 1
        return result

    def check(self, x, m, nums):
        s, c = 0, 1
        for num in nums:
            if s + num > x:
                c += 1
                s = num
            else:
                s += num
        return c <= m
