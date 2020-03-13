# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 上午10:30
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 01.01.py
# @Desc    : 说明

class Solution:
    def isUnique(self, astr: str) -> bool:
        charSet = set()
        for c in astr:
            if c not in charSet:
                charSet.add(c)
            else:
                return False
        return True
