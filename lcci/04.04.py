# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 上午11:04
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 04.04.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = True

    def isBalanced(self, root: TreeNode) -> bool:
        self.helper(root)
        return self.result

    def helper(self, root: TreeNode):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)
        if abs(left - right) > 1:
            self.result = False
        return max(left, right) + 1
