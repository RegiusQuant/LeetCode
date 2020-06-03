# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 上午7:51
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0837.py
# @Desc    : 说明

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W + 1)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        dp[K - 1] = min(N - K + 1, W) / W
        for i in reversed(range(K - 1)):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.new21Game(10, 1, 10))
    print(solution.new21Game(6, 1, 10))
    print(solution.new21Game(21, 17, 10))
