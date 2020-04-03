# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 上午10:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 05.07.py
# @Desc    : 说明

class Solution:
    def exchangeBits(self, num: int) -> int:
        return ((num >> 1) & 0x55555555) | ((num << 1) & 0xaaaaaaaa)
