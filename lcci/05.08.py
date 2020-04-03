# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 上午10:45
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 05.08.py
# @Desc    : 说明

from typing import List


class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        result = [0] * length
        width = w // 32
        n1, m1 = divmod(x1, 32)
        n2, m2 = divmod(x2, 32)
        for i in range(width * y + n1, width * y + n2 + 1):
            result[i] = -1

        if m1 != 0:
            result[width * y + n1] += 1 << (32 - m1)
        result[width * y + n2] -= (1 << (32 - m2 - 1)) - 1
        return result
