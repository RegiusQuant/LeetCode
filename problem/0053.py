# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 下午9:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0053.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        tmp, ret = 0, nums[0]
        for x in nums:
            tmp += x
            ret = max(ret, tmp)
            tmp = max(tmp, 0)
        return ret


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))
