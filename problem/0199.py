# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 上午10:37
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0199.py
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        depthRight, maxDepth = {}, -1
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if node:
                maxDepth = max(depth, maxDepth)
                depthRight[depth] = node.val
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        return [depthRight[d] for d in range(maxDepth + 1)]
