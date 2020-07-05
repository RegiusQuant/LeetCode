# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 下午2:12
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        right = [n - right[i] for i in range(len(right))]
        if len(left) == 0:
            return max(right)
        if len(right) == 0:
            return max(left)
        return max(max(left), max(right))
