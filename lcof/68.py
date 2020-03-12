# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 上午10:43
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 68.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.result

    def dfs(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if not node:
            return 0

        count = 0
        if node.val == p.val:
            count += 1
        if node.val == q.val:
            count += 1
        count += self.dfs(node.left, p, q)
        count += self.dfs(node.right, p, q)
        if count == 2 and not self.result:
            self.result = node
        return count
