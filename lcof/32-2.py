# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 上午10:15
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 32-2.py
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result, q = [], deque()
        q.append((0, root))
        while q:
            dep, node = q.popleft()
            if len(result) == dep:
                result.append([])
            result[dep].append(node.val)
            if node.left is not None:
                q.append((dep + 1, node.left))
            if node.right is not None:
                q.append((dep + 1, node.right))
        return result
