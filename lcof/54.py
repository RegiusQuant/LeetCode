# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 上午10:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 54.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0
        self.result = -1

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.count = k
        self.helper(root)
        return self.result

    def helper(self, node: TreeNode):
        if node:
            self.helper(node.right)
            if self.count == 1:
                self.result = node.val
                self.count -= 1
                return
            self.count -= 1
            self.helper(node.left)
