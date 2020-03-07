# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 下午12:59
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 59-2.py
# @Desc    : 说明

from collections import deque


class MaxQueue:

    def __init__(self):
        self.data = deque()
        self.helper = deque()

    def max_value(self) -> int:
        if not self.data:
            return -1
        return self.helper[0]

    def push_back(self, value: int) -> None:
        self.data.append(value)
        while self.helper and self.helper[-1] < value:
            self.helper.pop()
        self.helper.append(value)

    def pop_front(self) -> int:
        if not self.data:
            return -1
        value = self.data.popleft()
        if value == self.helper[0]:
            self.helper.popleft()
        return value
