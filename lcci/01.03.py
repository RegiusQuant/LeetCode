# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 下午2:48
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 01.03.py
# @Desc    : 说明

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(' ', '%20')
