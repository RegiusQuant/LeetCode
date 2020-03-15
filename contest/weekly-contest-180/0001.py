# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 下午6:37
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowMins = {min(r) for r in matrix}
        colMaxs = {max(c) for c in zip(*matrix)}
        return list(rowMins & colMaxs)
