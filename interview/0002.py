# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午1:40
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(len(nums)) if i % 2 == 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.arrayPairSum([1, 4, 3, 2]))
