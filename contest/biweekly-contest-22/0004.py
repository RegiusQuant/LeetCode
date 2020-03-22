# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        m, n = len(slices), len(slices) // 3
        t1 = self.helper(slices, m, n)
        t2 = self.helper(slices[1:] + [slices[0]], m, n)
        return max(t1, t2)

    def helper(self, slices, m, n):
        dp = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(1, n + 1):
                if i == 0:
                    dp[i][j] = slices[0]
                elif i == 1:
                    dp[i][j] = max(slices[0], slices[1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + slices[i])
        return dp[m - 2][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSizeSlices([1, 2, 3, 4, 5, 6]))
    print(solution.maxSizeSlices([8, 9, 8, 6, 1, 1]))
    print(solution.maxSizeSlices([4, 1, 2, 5, 8, 3, 1, 9, 7]))
    print(solution.maxSizeSlices([3, 1, 2]))
