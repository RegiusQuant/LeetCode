# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 下午6:41
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0106.py
# @Desc    : 说明

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        pos, root = inorder.index(postorder[-1]), TreeNode(postorder[-1])
        root.left = self.buildTree(inorder[:pos], postorder[:pos])
        root.right = self.buildTree(inorder[pos + 1:], postorder[pos:-1])
        return root
