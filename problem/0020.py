# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 下午5:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0020.py
# @Desc    : 说明

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {']': '[', ')': '(', '}': '{'}
        for x in s:
            if x not in match:
                stack.append(x)
            elif not stack or match[x] != stack.pop():
                return False
        return not stack
