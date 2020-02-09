# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 下午3:42
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0128.py.py
# @Desc    : 说明

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result, dp = 0, dict()
        for num in nums:
            if num not in dp:
                l, r = dp.get(num - 1, 0), dp.get(num + 1, 0)
                dp[num] = dp[num - l] = dp[num + r] = 1 + l + r
        return 0 if not nums else max(dp.values())


if __name__ == '__main__':
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(solution.longestConsecutive(nums))
