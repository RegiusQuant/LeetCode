# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 下午12:54
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0215.py
# @Desc    : 说明

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        pivot = nums[mid]
        nums[mid], nums[right] = nums[right], pivot

        pos = left
        for i in range(left, right):
            if nums[i] > pivot:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        nums[pos], nums[right] = nums[right], nums[pos]

        if k == pos + 1:
            return nums[pos]
        elif k < pos + 1:
            return self.findKthLargest(nums[:pos], k)
        else:
            return self.findKthLargest(nums[pos + 1:], k - pos - 1)
