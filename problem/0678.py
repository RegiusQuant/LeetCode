# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 下午12:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0678.py
# @Desc    : 说明

class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                if lo > 0:
                    lo -= 1
                hi -= 1
                if hi < 0:
                    return False
            else:
                if lo > 0:
                    lo -= 1
                hi += 1
        return lo == 0
