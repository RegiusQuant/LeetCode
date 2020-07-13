# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 下午10:08
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0350.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        result = []
        for x in nums2:
            if counter[x] > 0:
                result.append(x)
                counter[x] -= 1
        return result
