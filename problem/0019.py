# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 下午5:15
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0019.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        for i in range(n):
            if not temp:
                return head
            temp = temp.next

        curr, prev = head, None
        while temp:
            curr, prev, temp = curr.next, curr, temp.next

        if not prev:
            return curr.next
        else:
            prev.next = curr.next
            return head
