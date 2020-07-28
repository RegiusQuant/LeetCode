# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 下午10:02
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0392.py
# @Desc    : 说明

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        p1 = p2 = 0
        while p1 < n and p2 < m:
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        return p1 == n
