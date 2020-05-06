# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 上午11:08
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1049.py
# @Desc    : 说明

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n, s = len(stones), sum(stones)
        dp = [0] * (s // 2 + 1)
        for i in range(n):
            for j in range(s // 2, 0, -1):
                if j - stones[i] >= 0:
                    dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
                else:
                    break
        return s - 2 * dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.lastStoneWeightII([2, 7, 4, 1, 8, 1]))
