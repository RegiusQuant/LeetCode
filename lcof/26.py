# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 上午10:14
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 26.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return self.isMatch(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def isMatch(self, A: TreeNode, B: TreeNode) -> bool:
        if not A:
            return False
        if A.val == B.val:
            result = True
            if B.left is not None:
                result &= self.isMatch(A.left, B.left)
            if B.right is not None:
                result &= self.isMatch(A.right, B.right)
            return result
        return False