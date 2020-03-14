# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 下午2:52
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 01.04.py
# @Desc    : 说明

from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        oddCount = 0
        for v in counter.values():
            if v % 2:
                oddCount += 1
        return oddCount <= 1
