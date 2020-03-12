# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 上午10:38
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 67.py
# @Desc    : 说明

import re


class Solution:
    def strToInt(self, str: str) -> int:
        try:
            result = int(re.match('[\+\-]?\d+', str.strip()).group(0))
        except:
            return 0
        return min(max(result, -(1 << 31)), (1 << 31) - 1)
