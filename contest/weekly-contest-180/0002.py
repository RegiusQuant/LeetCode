# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 下午6:43
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return
        self.stack.append([x, 0])

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        x, v = self.stack.pop()
        if len(self.stack) > 0:
            self.stack[-1][1] += v
        return x + v

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) > 0:
            k = min(k - 1, len(self.stack) - 1)
            self.stack[k][1] += val
