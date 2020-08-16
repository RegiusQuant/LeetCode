# -*- coding: utf-8 -*-
# @Time       : 2020/08/17 01:09:15
# @Author     : RegiusQuant <315135833@qq.com>
# @Project    : LeetCode
# @File       : 0110.py
# @Description: 文件说明


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root)[1]

    def dfs(self, root):
        if not root:
            return 0, True

        left_height, left_flag = self.dfs(root.left)
        right_height, right_flag = self.dfs(root.right)
        if abs(left_height - right_height) >= 2 or not (left_flag and right_flag):
            return max(left_height, right_height) + 1, False
        else:
            return max(left_height, right_height) + 1, True
