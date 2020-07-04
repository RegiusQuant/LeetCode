# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 下午10:18
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0032.py
# @Desc    : 说明

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i - 2 >= 0 else 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestValidParentheses('())'))
    print(solution.longestValidParentheses(')()())'))
