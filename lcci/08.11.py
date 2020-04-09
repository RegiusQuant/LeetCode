# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 上午10:41
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.11.py
# @Desc    : 说明

class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [1] * (n + 1)

        for c in [5, 10, 25]:
            for i in range(c, n + 1):
                dp[i] = (dp[i] + dp[i - c]) % int(1e9 + 7)
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.waysToChange(10))
