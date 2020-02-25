# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 上午10:56
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 34.py
# @Desc    : 说明

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return self.result
        self.helper(0, sum, root, [])
        return self.result

    def helper(self, currSum: int, totalSum: int, node: TreeNode, currPath: List[int]):
        currSum += node.val
        currPath.append(node.val)

        if currSum == totalSum and not node.left and not node.right:
            self.result.append(currPath.copy())
            return
        if node.left:
            self.helper(currSum, totalSum, node.left, currPath.copy())
        if node.right:
            self.helper(currSum, totalSum, node.right, currPath.copy())


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    print(solution.pathSum(root, 13))