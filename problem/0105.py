# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 下午9:30
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0105.py
# @Desc    : 说明

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        pos, root = inorder.index(preorder[0]), TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:pos + 1], inorder[:pos])
        root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])
        return root
