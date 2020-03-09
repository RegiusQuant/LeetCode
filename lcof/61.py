# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 上午10:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 61.py
# @Desc    : 说明

from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        numZeros = sum([1 for x in nums if x == 0])
        numDiff = 0
        for i in range(1, 5):
            if nums[i] != 0 and nums[i] == nums[i - 1]:
                return False
            if nums[i - 1] != 0:
                numDiff += nums[i] - nums[i - 1] - 1
        return numDiff <= numZeros


if __name__ == '__main__':
    solution = Solution()
    print(solution.isStraight([1, 2, 3, 4, 5]))
    print(solution.isStraight([0, 0, 1, 2, 5]))
