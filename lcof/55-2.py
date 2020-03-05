# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 上午8:58
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 55-2.py
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

    def helper(self, node: TreeNode):
        if not node:
            return 0
        leftDep = self.helper(node.left)
        rightDep = self.helper(node.right)
        if abs(leftDep - rightDep) > 1:
            self.result = False
        return max(leftDep, rightDep) + 1
