# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 上午10:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 63.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        result, temp = 0, prices[0]
        for p in prices[1:]:
            temp = min(temp, p)
            result = max(result, p - temp)
        return result
