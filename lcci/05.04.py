# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 上午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 05.04.py
# @Desc    : 说明

from typing import List


class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        n = bin(num).count('1')
        left, right = num + 1, num - 1
        while bin(left).count('1') != n:
            left += 1
        while right and bin(right).count('1') != n:
            right -= 1
        right = -1 if right == 0 else right
        return left, right
