# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 下午7:33
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0146.py
# @Desc    : 说明

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capactity = capacity
        self.data = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.data and len(self.data) == self.capactity:
            self.data.popitem(last=False)
        self.data[key] = value
        self.data.move_to_end(key)