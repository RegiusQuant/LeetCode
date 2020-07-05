# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 下午2:09
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != arr[1] - arr[0]:
                return False
        return True
