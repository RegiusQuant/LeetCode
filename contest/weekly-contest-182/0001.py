# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 上午11:34
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = -1
        counter = Counter(arr)
        for k, v in counter.items():
            if k == v:
                result = max(result, k)
        return result
