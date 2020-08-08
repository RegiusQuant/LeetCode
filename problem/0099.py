# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 下午11:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0099.py
# @Desc    : 说明


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.first = self.second = None
        self.prev = TreeNode(float('-inf'))

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def traverse(self, root):
        if root is None:
            return

        self.traverse(root.left)
        if self.first is None and self.prev.val > root.val:
            self.first = self.prev
        if self.first is not None and self.prev.val > root.val:
            self.second = root
        self.prev = root
        self.traverse(root.right)
