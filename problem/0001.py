# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 下午12:31
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, x in enumerate(nums):
            if target - x in s:
                return [i, s[target - x]]
            s[x] = i
        return []
