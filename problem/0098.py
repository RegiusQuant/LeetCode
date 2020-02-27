# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 下午3:21
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0098.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root, None, None)

    def check(self, node: TreeNode, minVal, maxVal):
        if not node:
            return True
        if minVal is not None and node.val <= minVal:
            return False
        if maxVal is not None and node.val >= maxVal:
            return False
        return (self.check(node.left, minVal, node.val) and
                self.check(node.right, node.val, maxVal))
