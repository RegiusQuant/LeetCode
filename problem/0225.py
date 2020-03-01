# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 下午12:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0225.py
# @Desc    : 说明

from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def shift_to_last(self):
        length = len(self.data)
        for i in range(length - 1):
            self.data.append(self.data.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.shift_to_last()
        return self.data.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        self.shift_to_last()
        result = self.data.popleft()
        self.data.append(result)
        return result

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.data) == 0


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.top())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.empty())
