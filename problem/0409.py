# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 上午10:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0409.py
# @Desc    : 说明

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter, result = Counter(s), 0
        for v in counter.values():
            result += v // 2 * 2
        return result + 1 if result < len(s) else result
