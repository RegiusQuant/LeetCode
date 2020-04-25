# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 下午12:48
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0046.py
# @Desc    : 说明

from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.helper(nums, [])
        return self.result

    def helper(self, nums: List[int], curr: List[int]):
        if len(nums) == 0:
            self.result.append(curr)
            return
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i + 1:], curr + [nums[i]])


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
