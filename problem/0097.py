# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 下午10:36
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0097.py
# @Desc    : 说明


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, t = len(s1), len(s2), len(s3)
        if n + m != t:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(n + 1):
                p = i + j - 1
                if i > 0:
                    dp[i][j] |= (dp[i - 1][j] and s1[i - 1] == s3[p])
                if j > 0:
                    dp[i][j] |= (dp[i][j - 1] and s2[j - 1] == s3[p])
        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))