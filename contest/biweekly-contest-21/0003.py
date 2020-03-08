# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = 0

    def longestZigZag(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.result - 1

    def dfs(self, node: TreeNode):
        if not node:
            return 0, 0
        left1, left2 = self.dfs(node.left)
        right1, right2 = self.dfs(node.right)
        left = left2 + 1
        right = right1 + 1
        self.result = max(self.result, left, right)
        return left, right

