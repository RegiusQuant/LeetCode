# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午3:02
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0639.py
# @Desc    : 说明

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(len(s)):
            dp[i + 1] += dp[i] * self.calcNum(s[i])
            if i >= 1:
                dp[i + 1] += dp[i - 1] * self.calcNum(s[i - 1:i + 1])
            dp[i + 1] %= int(1e9 + 7)
        return dp[-1]

    def calcNum(self, s):
        if len(s) == 1:
            if s[0] == '*':
                return 9
            if '1' <= s[0] <= '9':
                return 1
            return 0
        else:
            if s == '**':
                return 15
            elif s[0] == '*':
                if '0' <= s[1] <= '6':
                    return 2
                else:
                    return 1
            elif s[1] == '*':
                if s[0] == '1':
                    return 9
                elif s[0] == '2':
                    return 6
                else:
                    return 0
            elif '10' <= s <= '26':
                return 1
            return 0


if __name__ == '__main__':
    solution = Solution()
    # print(solution.numDecodings('*'))
    # print(solution.numDecodings('1*'))
    # print(solution.numDecodings('**'))
    # print(solution.numDecodings('3*'))
    # print(solution.numDecodings('*1'))
    # print(solution.numDecodings('*1*1*0'))
    # print(solution.numDecodings('2*'))
    print(solution.numDecodings('*******'))