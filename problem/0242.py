# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 下午2:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0242.py
# @Desc    : 说明

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
