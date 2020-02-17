# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 下午8:12
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 09.py
# @Desc    : 说明

class CQueue:

    def __init__(self):
        self.stack1, self.stack2 = [], []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if not self.stack1:
            return -1
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        result = self.stack1.pop()
        self.stack1 = []
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return result


if __name__ == '__main__':
    obj = CQueue()
    obj.appendTail(3)
    print(obj.deleteHead())
    print(obj.deleteHead())
