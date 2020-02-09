# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 下午7:12
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0023.py
# @Desc    : 说明

from typing import List
from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TupleHelper(tuple):

    def __lt__(self, other):
        return self[0] < other[0]

    def __gt__(self, other):
        return self[0] > other[0]

    def __le__(self, other):
        return self[0] <= other[0]

    def __ge__(self, other):
        return self[0] >= other[0]


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        head = curr = ListNode(0)
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put(TupleHelper((node.val, node)))
        while not q.empty():
            val, node = q.get()
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node:
                q.put(TupleHelper((node.val, node)))
        return head.next


if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeKLists([[]]))
