# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 下午9:59
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0095.py
# @Desc    : 说明

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None, ]

        result = []
        for i in range(start, end + 1):
            t1 = self.helper(start, i - 1)
            t2 = self.helper(i + 1, end)

            for l in t1:
                for r in t2:
                    curr = TreeNode(i)
                    curr.left = l
                    curr.right = r
                    result.append(curr)
        return result
