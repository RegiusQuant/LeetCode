# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 上午9:57
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0121.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        temp, result = prices[0], 0
        for p in prices:
            temp = min(temp, p)
            result = max(result, p - temp)
        return result
