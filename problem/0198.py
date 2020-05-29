# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 下午7:38
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0198.py
# @Desc    : 说明

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([1, 2, 3, 1]))
    print(solution.rob([2, 7, 9, 3, 1]))
    print(solution.rob([2, 1, 1, 2]))
