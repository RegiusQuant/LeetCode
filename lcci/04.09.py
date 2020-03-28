# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 下午3:06
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 04.09.py
# @Desc    : 说明

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        self.helper(root, [], [root.val])
        return self.result

    def helper(self, node: TreeNode, temp: List, path: List):
        if node.left:
            temp.append(node.left)
        if node.right:
            temp.append(node.right)

        if not temp:
            self.result.append(path)

        for i, c in enumerate(temp):
            nt = temp[:i] + temp[i + 1:]
            self.helper(c, nt, path + [c.val])


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(solution.BSTSequences(root))
