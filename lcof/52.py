# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 上午8:39
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 52.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa
