# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 上午10:14
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0101.py
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
        return self.check(root.left, root.right)

    def check(self, p, q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.check(p.left, q.right) and self.check(p.right, q.left)
        return False
