# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 上午12:17
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0044.py
# @Desc    : 说明

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] | dp[i][j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch('aa', 'a'))
    print(solution.isMatch('aa', '*'))
    print(solution.isMatch('cb', '?a'))
    print(solution.isMatch('adceb', 'a*b'))
    print(solution.isMatch('acdcb', 'a*c?b'))
