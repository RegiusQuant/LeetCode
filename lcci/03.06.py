# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 上午10:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 03.06.py
# @Desc    : 说明

from typing import List
from collections import deque


class AnimalShelf:

    def __init__(self):
        self.count = 0
        self.data = [deque(), deque()]

    def enqueue(self, animal: List[int]) -> None:
        self.data[animal[1]].append((animal[0], self.count))
        self.count += 1

    def dequeueAny(self) -> List[int]:
        if len(self.data[0]) + len(self.data[1]) == 0:
            return [-1, -1]

        if len(self.data[0]) == 0:
            t = 1
        elif len(self.data[1]) == 0:
            t = 0
        else:
            t = int(self.data[0][0][0] > self.data[1][0][0])
        a = self.data[t].popleft()
        return [a[0], t]

    def dequeueDog(self) -> List[int]:
        if len(self.data[1]) == 0:
            return [-1, -1]
        a = self.data[1].popleft()
        return [a[0], 1]

    def dequeueCat(self) -> List[int]:
        if len(self.data[0]) == 0:
            return [-1, -1]
        a = self.data[0].popleft()
        return [a[0], 0]


if __name__ == '__main__':
    obj = AnimalShelf()
    obj.enqueue([0, 0])
    obj.enqueue([1, 1])
    obj.enqueue([2, 0])
    print(obj.dequeueAny())
    print(obj.dequeueAny())
    print(obj.dequeueAny())
