# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 下午3:02
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 04.08.py
# @Desc    : 说明

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root
