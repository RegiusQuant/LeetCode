# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 上午10:05
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 02.03.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next