# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 上午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 02.04.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        hl, hr = ListNode(0), ListNode(0)
        left, right, node = hl, hr, head
        while node:
            if node.val < x:
                left.next = node
                left = left.next
            else:
                right.next = node
                right = right.next
            node = node.next
        left.next, right.next = hr.next, None
        return hl.next
