# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 下午9:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0337.py
# @Desc    : 说明


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))

    def dfs(self, root: TreeNode):
        if not root:
            return 0, 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (
            root.val + left[1] + right[1],
            max(left) + max(right)
        )
