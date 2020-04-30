# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午1:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0102.py
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

        result = []
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if depth == len(result):
                result.append([])
            result[depth].append(node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return result


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.levelOrder(root))
