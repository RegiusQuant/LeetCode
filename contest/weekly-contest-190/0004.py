# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 上午10:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        if max(nums1) < 0 and min(nums2) >= 0:
            return max(nums1) * min(nums2)
        elif max(nums2) < 0 and min(nums1) >= 0:
            return max(nums2) * min(nums1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1] + max(0, nums1[i - 1] * nums2[j - 1])
                )
        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDotProduct([2, 1, -2, 5], [3, 0, -6]))
    print(solution.maxDotProduct([3, -2], [2, -6, 7]))
    print(solution.maxDotProduct([-1, -1], [1, 1]))
    print(solution.maxDotProduct([6, 2], [-5, -3]))
