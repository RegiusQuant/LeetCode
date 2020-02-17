# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 下午8:02
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 07.py
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
        node, pos = TreeNode(preorder[0]), inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:pos + 1], inorder[:pos])
        node.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])
        return node


if __name__ == '__main__':
    solution = Solution()
    print(solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
