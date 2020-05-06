# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 上午10:44
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0034.py
# @Desc    : 说明

import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idxLeft = bisect.bisect_left(nums, target)
        if idxLeft == len(nums) or nums[idxLeft] != target:
            return [-1, -1]
        idxRight = bisect.bisect_right(nums, target)
        return [idxLeft, idxRight - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], target=7))
