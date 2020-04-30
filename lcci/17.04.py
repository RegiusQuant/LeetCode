# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 上午10:44
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 17.04.py
# @Desc    : 说明

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
