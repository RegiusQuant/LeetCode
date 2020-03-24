# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 上午10:32
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 03.04.py
# @Desc    : 说明

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        x = self.s1.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return x

    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        x = self.s1[0]
        while self.s2:
            self.s1.append(self.s2.pop())
        return x

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0


if __name__ == '__main__':
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())
