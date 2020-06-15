# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 下午9:49
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1143.py
# @Desc    : 说明

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonSubsequence('abcde', 'ace'))
