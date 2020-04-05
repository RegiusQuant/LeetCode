# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 上午10:18
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        stoneValue += [0] * 3
        dp, s = [0] * (n + 3), [0] * (n + 3)

        s[n - 1] = stoneValue[n - 1]
        for i in range(n - 2, -1, -1):
            s[i] = s[i + 1] + stoneValue[i]
        # print(s)

        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            for j in range(3):
                dp[i] = max(dp[i], sum(stoneValue[i: i + j + 1]) + s[i + j + 1] - dp[i + j + 1])
        # print(dp)
        if dp[0] > s[0] - dp[0]:
            return 'Alice'
        elif dp[0] == s[0] - dp[0]:
            return 'Tie'
        else:
            return 'Bob'


if __name__ == '__main__':
    solution = Solution()
    print(solution.stoneGameIII([1, 2, 3, 7]))
    print(solution.stoneGameIII([1, 2, 3, -9]))
    print(solution.stoneGameIII([1, 2, 3, 6]))
    print(solution.stoneGameIII([1, 2, 3, -1, -2, -3, 7]))
    print(solution.stoneGameIII([-1, -2, -3]))
