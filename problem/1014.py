# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 下午10:49
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1014.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        result, temp = 0, A[0] + 0
        for i in range(1, len(A)):
            result = max(result, temp + A[i] - i)
            temp = max(temp, A[i] + i)
        return result
