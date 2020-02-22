# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 上午10:59
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 30.py
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
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self) -> None:
        x = self.data.pop()
        if x == self.helper[-1]:
            self.helper.pop()

    def top(self) -> int:
        return self.data[-1]

    def min(self) -> int:
        return self.helper[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.min())
    minStack.pop()
    print(minStack.top())
    print(minStack.min())
