# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 下午10:03
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 17.13.py
# @Desc    : 说明

from typing import List


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = set(dictionary)

        n = len(sentence)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if sentence[j:i] in dictionary:
                    dp[i] = min(dp[i], dp[j])
        return dp[-1]
