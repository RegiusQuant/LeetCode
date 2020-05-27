# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 下午8:14
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0974.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        counter = Counter([0])
        result, s = 0, 0
        for x in A:
            s = (s + x) % K
            result += counter[s]
            counter[s] += 1
        return result
