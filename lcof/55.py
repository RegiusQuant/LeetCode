# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 上午10:38
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 55.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
