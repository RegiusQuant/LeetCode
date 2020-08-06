# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 下午9:10
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0336.py
# @Desc    : 说明

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)

        def check(s, left, right):
            s = s[left: right + 1]
            return s == s[::-1]

        result = []
        revToIdx = {w[::-1]: i for i, w in enumerate(words)}
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if check(word, j, m - 1):
                    leftId = revToIdx.get(word[0: j], -1)
                    if leftId != -1 and leftId != i:
                        result.append([i, leftId])
                if j and check(word, 0, j - 1):
                    rightId = revToIdx.get(word[j: m], -1)
                    if rightId != -1 and rightId != i:
                        result.append([rightId, i])
        return result
