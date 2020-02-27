# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 上午10:47
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 42.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result, tmp = nums[0], nums[0]
        for x in nums[1:]:
            tmp = max(x, tmp + x)
            result = max(result, tmp)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
