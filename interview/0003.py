# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午2:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
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
        if not postorder:
            return None

        pos = inorder.index(postorder[-1])
        node = TreeNode(postorder[-1])
        node.left = self.buildTree(inorder[:pos], postorder[:pos])
        node.right = self.buildTree(inorder[pos + 1:], postorder[pos:-1])
        return node
