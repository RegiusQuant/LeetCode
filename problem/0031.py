# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 上午10:54
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0031.py
# @Desc    : 说明

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = len(nums) - 2
        while p >= 0 and nums[p] >= nums[p + 1]:
            p -= 1
        if p >= 0:
            q = len(nums) - 1
            while q >= 0 and nums[q] <= nums[p]:
                q -= 1
            nums[p], nums[q] = nums[q], nums[p]
        nums[p + 1:] = reversed(nums[p + 1:])


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    solution.nextPermutation(nums)
    print(nums)
