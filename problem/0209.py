# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 下午1:10
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0209.py
# @Desc    : 说明

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        result = float('inf')
        left, right, total = 0, 0, 0
        while right < n:
            total += nums[right]
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return result if result != float('inf') else 0
