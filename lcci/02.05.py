# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 上午10:34
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 02.05.py
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
            if l1 and l2:
                t = l1.val + l2.val + carry
                l1, l2 = l1.next, l2.next
            elif l1:
                t = l1.val + carry
                l1 = l1.next
            else:
                t = l2.val + carry
                l2 = l2.next
            curr.next = ListNode(t % 10)
            curr = curr.next
            carry = t // 10
        if carry != 0:
            curr.next = ListNode(carry)
        return head.next
