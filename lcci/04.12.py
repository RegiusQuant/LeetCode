# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 下午1:13
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 04.12.py
# @Desc    : 说明

from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        sumCount = Counter({0: 1})
        return self.helper(root, sumCount, sum, 0)

    def helper(self, root, sumCount, sum, cur):
        if not root:
            return 0

        result = 0
        cur += root.val
        result += sumCount[cur - sum]
        sumCount[cur] += 1

        result += self.helper(root.left, sumCount, sum, cur)
        result += self.helper(root.right, sumCount, sum, cur)
        sumCount[cur] -= 1
        return result
