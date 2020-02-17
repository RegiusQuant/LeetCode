# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 下午6:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 03.py
# @Desc    : 说明

from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        numSet = set()
        for x in nums:
            if x in numSet:
                return x
            numSet.add(x)
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
    print(solution.findRepeatNumber([0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
