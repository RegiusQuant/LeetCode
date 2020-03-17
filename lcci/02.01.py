# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 上午10:38
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 02.01.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        temp, valSet = head, set()
        while temp:
            valSet.add(temp.val)
            while temp.next and temp.next.val in valSet:
                temp.next = temp.next.next
            temp = temp.next
        return head