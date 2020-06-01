# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 上午9:17
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1431.py
# @Desc    : 说明

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxVal = max(candies)
        result = []
        for c in candies:
            if c + extraCandies >= maxVal:
                result.append(True)
            else:
                result.append(False)
        return result
