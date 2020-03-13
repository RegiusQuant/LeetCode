# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 上午10:32
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 01.02.py
# @Desc    : 说明

from collections import Counter


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)
