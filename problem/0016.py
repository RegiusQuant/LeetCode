# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 下午6:15
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0016.py
# @Desc    : 说明

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if abs(temp - target) < abs(result - target):
                    result = temp
                    if temp == target:
                        return target

                if temp < target:
                    left += 1
                else:
                    right -= 1
        return result
