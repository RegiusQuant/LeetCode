# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 下午6:04
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0222.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = self.computeDepth(root)
        if depth == 0:
            return 1

        left, right = 1, 2 ** depth - 1
        while left <= right:
            mid = (left + right) // 2
            if self.check(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1
        return (2 ** depth - 1) + left

    def computeDepth(self, node: TreeNode) -> int:
        result = 0
        while node.left:
            node = node.left
            result += 1
        return result

    def check(self, idx, depth, node):
        left, right = 0, 2 ** depth - 1
        for _ in range(depth):
            mid = (left + right) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None
