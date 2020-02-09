# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 下午4:45
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0226.py
# @Desc    : 说明

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
