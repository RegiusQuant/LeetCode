# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 上午9:59
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0543.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.result - 1

    def dfs(self, node: TreeNode):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.result = max(self.result, left + right + 1)
        return max(left, right) + 1
