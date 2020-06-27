# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 上午10:57
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0041.py
# @Desc    : 说明

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1

        for i in range(len(nums)):
            x = abs(nums[i])
            if x <= len(nums):
                nums[x - 1] = -abs(nums[x - 1])

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1
