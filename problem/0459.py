# -*- coding: utf-8 -*-
# @Time       : 2020/08/24 23:27:56
# @Author     : RegiusQuant <315135833@qq.com>
# @Project    : LeetCode
# @File       : 0459.py
# @Description: 文件说明


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
