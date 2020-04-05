# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 下午1:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0460.py
# @Desc    : 说明

from collections import defaultdict


class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 0
        self.prev = None
        self.next = None

    def insert(self, node):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node


def create():
    head = ListNode(0, 0)
    tail = ListNode(0, 0)
    head.next = tail
    tail.prev = head
    return head, tail


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.minFreq = 0
        self.freqMap = defaultdict(create)
        self.keyMap = {}

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
            if node.prev is self.freqMap[0]:
                self.freqMap.pop(node.freq)
        return node.key

    def increase(self, node):
        node.freq += 1
        self.delete(node)
        self.freqMap[node.freq][-1].prev.insert(node)
        if node.freq == 1:
            self.minFreq = 1
        elif self.minFreq == node.freq - 1:
            head, tail = self.freqMap[node.freq - 1]
            if head.next == tail:
                self.minFreq = node.freq

    def get(self, key: int) -> int:
        if key in self.keyMap:
            self.increase(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap != 0:
            if key in self.keyMap:
                node = self.keyMap[key]
                node.val = value
            else:
                node = ListNode(key, value)
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.cap:
                self.size -= 1
                delete = self.delete(self.freqMap[self.minFreq][0].next)
                self.keyMap.pop(delete)
            self.increase(node)
