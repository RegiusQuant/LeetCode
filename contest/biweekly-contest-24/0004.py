# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 下午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明


class Solution:

    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0] * len(s)
        dp[-1] = 1 if 0 < int(s[-1]) <= k else 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                continue
            if len(s) - i <= len(str(k)) and int(s[i:]) <= k:
                dp[i] = 1
            for j in range(i + 1, len(s)):
                if int(s[i:j]) > k:
                    break
                dp[i] = (dp[i] + dp[j]) % int(1e9 + 7)
        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfArrays('1000', 10000))
    print(solution.numberOfArrays('1000', 10))
    print(solution.numberOfArrays('1317', 2000))
    print(solution.numberOfArrays('2020', 30))
    print(solution.numberOfArrays('1234567890', 90))
