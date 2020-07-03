# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 上午9:00
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0108.py
# @Desc    : 说明

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        p = len(nums) // 2
        node = TreeNode(nums[p])
        node.left = self.sortedArrayToBST(nums[:p])
        node.right = self.sortedArrayToBST(nums[p + 1:])
        return node
