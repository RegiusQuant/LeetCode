# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 上午10:34
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 03.03.py
# @Desc    : 说明

class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.pos = 0
        self.count = 0
        self.data = []

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        if self.pos + 1 > len(self.data):
            self.data.append([])
        self.data[self.pos].append(val)
        if len(self.data[self.pos]) == self.cap:
            self.pos += 1
        self.count += 1

    def pop(self) -> int:
        if self.count == 0:
            return -1
        if self.pos + 1 > len(self.data):
            self.pos -= 1
        x = self.data[self.pos].pop()
        if len(self.data[self.pos]) == 0:
            self.data.pop()
            if self.pos > 0 and len(self.data[self.pos - 1]) < self.cap:
                self.pos -= 1
        self.count -= 1
        return x

    def popAt(self, index: int) -> int:
        if index >= len(self.data):
            return -1
        x = self.data[index].pop()
        if len(self.data[index]) == 0:
            self.data.pop(index)
            self.pos -= 1
        self.count -= 1
        if self.count == 0:
            self.pos = 0
        return x


if __name__ == '__main__':

    opts = ["StackOfPlates", "pop", "popAt", "push", "popAt", "popAt", "pop", "pop", "push", "popAt", "pop", "push",
            "push",
            "pop", "popAt", "popAt", "push", "push", "push", "popAt", "pop", "pop", "pop", "popAt", "pop", "push",
            "popAt",
            "push", "push", "popAt", "push", "push", "pop", "popAt", "push", "pop", "popAt", "push", "pop", "push",
            "pop",
            "popAt", "popAt", "pop", "push", "push", "pop", "popAt", "push", "push", "pop", "pop", "popAt"]
    params = [[3], [], [1], [1], [2], [2], [], [], [9], [3], [], [51], [20], [], [2], [0], [35], [1], [19], [3], [], [],
              [], [1],
              [], [36], [1], [19], [3], [3], [15], [44], [], [3], [46], [], [0], [42], [], [31], [], [0], [2], [], [10],
              [49],
              [], [1], [14], [50], [], [], [3]]

    sop = None
    for o, p in zip(opts, params):
        print('OPT:', o, p)
        if o == 'StackOfPlates':
            sop = StackOfPlates(p[0])
        elif o == 'pop':
            print(sop.pop())
        elif o == 'popAt':
            print(sop.popAt(p[0]))
        else:
            sop.push(p[0])

        print('SOP:', sop.data, sop.count, sop.pos)
