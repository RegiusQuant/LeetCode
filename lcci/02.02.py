# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 上午10:02
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 02.02.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        curr = head
        for _ in range(k):
            head = head.next
        while head:
            head = head.next
            curr = curr.next
        return curr.val
