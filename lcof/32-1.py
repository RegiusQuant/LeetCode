# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 上午10:05
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 32-1.py
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
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result, q = [], deque()
        q.append(root)
        while q:
            node = q.popleft()
            result.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return result
