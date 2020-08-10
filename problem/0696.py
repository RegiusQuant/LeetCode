# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 下午9:58
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0696.py
# @Desc    : 说明


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        p, r = 0, 0
        while p < len(s):
            x, c = s[p], 0
            while p < len(s) and s[p] == x:
                p += 1
                c += 1
            result += min(c, r)
            r = c
        return result
