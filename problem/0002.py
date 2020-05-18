# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 下午5:07
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        curr, carry = head, 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry, val = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            curr.next = ListNode(carry)
        return head.next
