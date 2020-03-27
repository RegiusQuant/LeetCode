# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 上午10:37
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 04.05.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root: TreeNode, lval, rval):
        if not root:
            return True
        return (lval < root.val < rval and
                self.helper(root.left, lval, root.val) and
                self.helper(root.right, root.val, rval))
