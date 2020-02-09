# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 下午3:12
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0155.py
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
        if len(self.helper) == 0 or x < self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        if self.data:
            self.data.pop()
            self.helper.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())

    obj = MinStack()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
