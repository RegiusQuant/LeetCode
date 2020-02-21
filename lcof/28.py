# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 上午10:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 28.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, leftNode: TreeNode, rightNode: TreeNode) -> bool:
        if leftNode is None and rightNode is None:
            return True
        elif leftNode is None or rightNode is None:
            return False
        elif leftNode.val != rightNode.val:
            return False
        return self.helper(leftNode.left, rightNode.right) and self.helper(leftNode.right, rightNode.left)
