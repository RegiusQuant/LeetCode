# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 下午4:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0124.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.result

    def helper(self, root: TreeNode):
        if not root:
            return 0

        leftVal = max(0, self.helper(root.left))
        rightVal = max(0, self.helper(root.right))
        self.result = max(self.result, leftVal + rightVal + root.val)
        return max(leftVal, rightVal) + root.val


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.maxPathSum(root))
