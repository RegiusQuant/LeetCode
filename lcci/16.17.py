# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 上午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.17.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result, curr = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr = max(0, curr) + nums[i]
            result = max(curr, result)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
