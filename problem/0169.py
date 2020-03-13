# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 上午10:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0169.py
# @Desc    : 说明

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
