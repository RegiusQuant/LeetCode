# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 下午2:43
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0820.py
# @Desc    : 说明

from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return sum(len(w) + 1 for w in s)
