# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 下午8:14
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0333.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = 0

    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.helper(root)
        return self.result

    def helper(self, root):
        if not root:
            return True, float('inf'), float('-inf'), 0

        leftResult, leftMin, leftMax, leftNum = self.helper(root.left)
        rightResult, rightMin, rightMax, rightNum = self.helper(root.right)
        if leftResult and rightResult:
            if leftMax < root.val < rightMin:
                self.result = max(self.result, leftNum + rightNum + 1)
                currMin = min(leftMin, rightMin, root.val)
                currMax = max(leftMax, rightMax, root.val)
                return True, currMin, currMax, leftNum + rightNum + 1
        return False, -1, -1, -1