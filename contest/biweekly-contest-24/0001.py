# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 下午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        x = min(nums)
        if x >= 1:
            return 1
        else:
            return -x + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.minStartValue([-3, 2, -3, 4, 2]))
    print(solution.minStartValue([1, 2]))
    print(solution.minStartValue([0, 0, 0]))
    print(solution.minStartValue([1, -2, -3]))
