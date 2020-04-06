# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 上午10:40
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0072.py
# @Desc    : 说明

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(
                    dp[i - 1][j - 1] + (1 if word1[i - 1] != word2[j - 1] else 0),
                    dp[i][j - 1] + 1,
                    dp[i - 1][j] + 1
                )
        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance('horse', 'ros'))
    print(solution.minDistance('', 'a'))