# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 下午9:31
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0152.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        minVal, maxVal, ret = 1, 1, nums[0]
        for x in nums:
            minVal, maxVal = (
                min(x, minVal * x, maxVal * x),
                max(x, minVal * x, maxVal * x)
            )
            ret = max(ret, maxVal)
        return ret


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, -2, 4]
    print(solution.maxProduct(nums))
    nums = [-2, 0, -1]
    print(solution.maxProduct(nums))
