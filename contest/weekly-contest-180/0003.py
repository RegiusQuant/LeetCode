# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 下午6:51
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.inorder = []

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorderTraversal(root)
        if len(self.inorder) < 3:
            return root
        return self.build(0, len(self.inorder) - 1)

    def build(self, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = self.inorder[mid]
        root.left = self.build(left, mid - 1)
        root.right = self.build(mid + 1, right)
        return root

    def inorderTraversal(self, root: TreeNode):
        if not root:
            return
        self.inorderTraversal(root.left)
        self.inorder.append(root)
        self.inorderTraversal(root.right)
