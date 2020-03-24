# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 上午10:56
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 03.05.py
# @Desc    : 说明

class SortedStack:

    def __init__(self):
        self.data = []
        self.helper = []

    def push(self, val: int) -> None:
        while self.helper and self.helper[-1] > val:
            self.data.append(self.helper.pop())
        while self.data and self.data[-1] < val:
            self.helper.append(self.data.pop())
        self.data.append(val)

    def pop(self) -> None:
        while self.helper:
            self.data.append(self.helper.pop())
        if self.data:
            self.data.pop()

    def peek(self) -> int:
        while self.helper:
            self.data.append(self.helper.pop())
        if not self.data:
            return -1
        return self.data[-1]

    def isEmpty(self) -> bool:
        return len(self.data) + len(self.helper) == 0


if __name__ == '__main__':
    stack = SortedStack()
    stack.push(1)
    stack.push(2)
    print(stack.peek())
    stack.pop()
    print(stack.peek())

    stack = SortedStack()
    stack.pop()
    stack.pop()
    stack.push(1)
    stack.pop()
    print(stack.isEmpty())