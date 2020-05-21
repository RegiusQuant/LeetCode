# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 下午4:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0953.py
# @Desc    : 说明

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda s: ''.join(['abcdefghijklmnopqrstuvwxyz'[order.index(i)] for i in s]))
