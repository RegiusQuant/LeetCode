# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 上午10:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 02.07.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        nodeA, nodeB = headA, headB
        countA, countB = 0, 0
        while nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next
            if not nodeA:
                nodeA = headB
                countA += 1
                if countA > 1:
                    return None
            if not nodeB:
                nodeB = headA
                countB += 1
                if countB > 1:
                    return None
        return nodeA
