# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 上午11:30
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 36.py
# @Desc    : 说明

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.head = self.prev = self.tail = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.helper(root)
        self.head.left = self.tail
        self.tail.right = self.head
        return self.head

    def helper(self, node: 'Node'):
        if not node:
            return None
        self.helper(node.left)
        if self.prev is None:
            self.head = node
        else:
            self.prev.right = node
        node.left = self.prev
        self.prev = self.tail = node
        self.helper(node.right)
