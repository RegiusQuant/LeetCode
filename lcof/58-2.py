# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 下午1:44
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 58-2.py
# @Desc    : 说明

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
