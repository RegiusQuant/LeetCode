# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 上午9:58
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0445.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        result, carry = None, 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            carry, cur = divmod(a + b + carry, 10)
            node = ListNode(cur)
            node.next = result
            result = node
        return result
