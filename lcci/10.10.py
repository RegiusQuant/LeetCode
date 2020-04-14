# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 上午10:14
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 10.10.py
# @Desc    : 说明

class BIT:

    def __init__(self, n):
        self.data = [0] * (n + 2)

    @staticmethod
    def _lowbit(x):
        return x & (-x)

    def update(self, index, delta):
        while index < len(self.data):
            self.data[index] += delta
            index += self._lowbit(index)

    def quary(self, index):
        result = 0
        while index > 0:
            result += self.data[index]
            index -= self._lowbit(index)
        return result


class StreamRank:

    def __init__(self):
        self.data = BIT(50000)

    def track(self, x: int) -> None:
        self.data.update(x + 1, 1)

    def getRankOfNumber(self, x: int) -> int:
        return self.data.quary(x + 1)
