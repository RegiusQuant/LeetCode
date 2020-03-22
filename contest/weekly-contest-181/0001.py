# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 下午1:26
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target


if __name__ == '__main__':
    solution = Solution()
    print(solution.createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
    print(solution.createTargetArray(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]))
