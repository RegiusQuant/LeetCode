# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 下午9:50
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0104.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, node, level):
        if not node:
            return level
        return max(self.dfs(node.left, level + 1), self.dfs(node.right, level + 1))
