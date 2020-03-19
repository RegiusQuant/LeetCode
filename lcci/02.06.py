# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 上午10:53
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 02.06.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        prev, slow, fast = None, head, head
        while fast and fast.next:
            curr = slow
            slow = slow.next
            fast = fast.next.next
            curr.next = prev
            prev = curr

        if fast:
            slow = slow.next

        while slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True
