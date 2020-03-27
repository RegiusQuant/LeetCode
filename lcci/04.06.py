# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 上午10:47
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 04.06.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = None

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.helper(root, p)
        if self.result:
            return self.result if self.result != p else None
        return None

    def helper(self, root: TreeNode, p: TreeNode):
        if not root:
            return
        self.helper(root.left, p)
        if self.result and self.result.val == p.val:
            self.result = root
        elif root.val == p.val:
            self.result = p
        self.helper(root.right, p)
