# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 上午10:26
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 10.11.py
# @Desc    : 说明

from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i % 2 == 0 and nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            elif i % 2 == 1 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]