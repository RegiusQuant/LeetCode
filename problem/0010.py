# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 下午8:04
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0010.py
# @Desc    : 说明

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def check(i, j):
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] |= dp[i][j - 2]
                    if check(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if check(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch('aa', 'a'))
    print(solution.isMatch('aa', 'a*'))
