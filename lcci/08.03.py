# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 上午11:12
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.03.py
# @Desc    : 说明

from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == nums[i]:
                return i
        return -1
