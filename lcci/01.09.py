# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 上午10:17
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 01.09.py
# @Desc    : 说明

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        return (s1 + s1).find(s2) >= 0
