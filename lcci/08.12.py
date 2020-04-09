# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 上午10:53
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.12.py
# @Desc    : 说明

from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.helper(0, n, [], [], [])
        return self.result

    def helper(self, x, n, usedCols, usedDiff1, usedDiff2):
        if x == n:
            self.result.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in usedCols])
            return

        for y in range(n):
            if y not in usedCols and (x + y) not in usedDiff1 and (x - y) not in usedDiff2:
                self.helper(x + 1, n, usedCols + [y], usedDiff1 + [x + y], usedDiff2 + [x - y])
