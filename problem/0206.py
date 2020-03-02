# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 上午10:03
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0206.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
