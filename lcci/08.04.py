# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 上午10:03
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.04.py
# @Desc    : 说明

from typing import List

class Solution:
    def __init__(self):
        self.result = []
        self.visit = set()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, 0, [])
        return self.result

    def helper(self, nums, x, temp):
        if x >= len(nums):
            if tuple(temp) not in self.visit:
                self.visit.add(tuple(temp))
                self.result.append(temp.copy())
            return

        temp.append(nums[x])
        self.helper(nums, x + 1, temp)
        temp.pop()
        self.helper(nums, x + 1, temp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))