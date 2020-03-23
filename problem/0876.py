# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 上午10:26
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0876.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
