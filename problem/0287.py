# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 下午7:42
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0287.py
# @Desc    : 说明

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right, result = 1, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            cnt = sum(1 for x in nums if x <= mid)
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1
                result = mid
        return result
