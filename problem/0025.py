# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 下午7:39
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0025.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        curr, ghead = head, self
        while curr:
            thead, prev, count = curr, None, 0

            temp = curr
            while count < k and temp:
                temp = temp.next
                count += 1

            if count == k:
                while count > 0 and curr:
                    curr.next, prev, curr = prev, curr, curr.next
                    count -= 1
                ghead.next = prev
                ghead = thead
            else:
                ghead.next = curr
                break
        return self.next
