# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 上午10:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 17.16.py
# @Desc    : 说明

from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        n = len(nums)
        dp = nums.copy()
        for i in range(2, n):
            for j in range(i - 1):
                dp[i] = max(dp[i], dp[j] + nums[i])
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.massage([1, 2, 3, 1]))
    print(solution.massage([2, 7, 9, 3, 1]))
    print(solution.massage([2, 1, 4, 5, 3, 1, 1, 3]))
