# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 下午4:18
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0094.py
# @Desc    : 说明

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(solution.inorderTraversal(root))
