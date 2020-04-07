# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 上午10:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.06.py
# @Desc    : 说明

from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        self.helper(len(A), A, B, C)

    def helper(self, n: int, A: List[int], B: List[int], C: List[int]):
        if n == 1:
            C.append(A[-1])
            A.pop()
            return
        self.helper(n - 1, A, C, B)
        C.append(A[-1])
        A.pop()
        self.helper(n - 1, B, A, C)
