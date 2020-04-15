# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 下午1:24
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.01.py
# @Desc    : 说明

from typing import List


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0], numbers[1] = numbers[1], numbers[0]
        return numbers
