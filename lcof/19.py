# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 下午1:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 19.py
# @Desc    : 说明

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if j >= 2:
                        dp[i][j] |= dp[i][j - 2]
                        if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                            dp[i][j] |= dp[i - 1][j]
        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch('aa', 'a'))
    print(solution.isMatch('aa', 'a*'))
    print(solution.isMatch('ab', '.*'))
    print(solution.isMatch('aaa', 'ab*ac*a'))
