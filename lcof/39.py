# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 上午10:37
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 39.py
# @Desc    : 说明

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
