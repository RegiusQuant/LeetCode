# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 上午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 03.02.py
# @Desc    : 说明

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) == 0 or self.helper[-1] >= x:
            self.helper.append(x)

    def pop(self) -> None:
        x = self.data.pop()
        if x == self.helper[-1]:
            self.helper.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.helper[-1]
