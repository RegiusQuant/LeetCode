# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 上午11:00
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0238.py
# @Desc    : 说明

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        result[0] = 1
        for i in range(1, n):
            result[i] = nums[i - 1] * result[i - 1]

        right = 1
        for i in reversed(range(n)):
            result[i] = result[i] * right
            right *= nums[i]
        return result
