# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 上午9:56
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 14-1.py
# @Desc    : 说明

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] = max(dp[i], dp[i - j] * j)
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.cuttingRope(2))
    print(solution.cuttingRope(10))
