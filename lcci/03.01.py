# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 上午10:53
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 03.01.py
# @Desc    : 说明

class TripleInOne:

    def __init__(self, stackSize: int):
        self.data = [0] * (stackSize * 3) + [stackSize, 2 * stackSize, stackSize, 0]

    def push(self, stackNum: int, value: int) -> None:
        p = self.data[-stackNum - 1]
        if p < (stackNum + 1) * self.data[-4]:
            self.data[p] = value
            self.data[-stackNum - 1] += 1

    def pop(self, stackNum: int) -> int:
        p = self.data[-stackNum - 1]
        if p > stackNum * self.data[-4]:
            self.data[-stackNum - 1] -= 1
            return self.data[p - 1]
        return -1

    def peek(self, stackNum: int) -> int:
        p = self.data[-stackNum - 1]
        if p > stackNum * self.data[-4]:
            return self.data[p - 1]
        return -1

    def isEmpty(self, stackNum: int) -> bool:
        p = self.data[-stackNum - 1]
        return p == stackNum * self.data[-4]


if __name__ == '__main__':
    stack = TripleInOne(1)
    stack.push(0, 1)
    stack.push(0, 2)
    print(stack.pop(0))
    print(stack.pop(0))
    print(stack.pop(0))
    print(stack.isEmpty(0))

    stack = TripleInOne(2)
    stack.push(0, 1)
    stack.push(0, 2)
    print(stack.pop(0))
    print(stack.pop(0))
    print(stack.pop(0))
    print(stack.peek(0))