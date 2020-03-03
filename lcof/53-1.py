# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 上午8:43
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 53-1.py
# @Desc    : 说明

from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target)


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([5, 7, 7, 8, 8, 10], 8))
    print(solution.search([5, 7, 7, 8, 8, 10], 6))
