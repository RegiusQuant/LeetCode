# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 下午1:01
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 04.10.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return self.checkSame(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

    def checkSame(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and self.checkSame(t1.left, t2.left) and self.checkSame(t1.right, t2.right)
