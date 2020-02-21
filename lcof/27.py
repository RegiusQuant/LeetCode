# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 上午10:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 27.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = root.right, root.left
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
        return root
