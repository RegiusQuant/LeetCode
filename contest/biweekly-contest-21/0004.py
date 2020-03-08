# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = 0

    def maxSumBST(self, root: TreeNode) -> int:
        self.helper(root)
        return self.result

    def helper(self, node: TreeNode):
        if not node:
            return 0, True
        flag = True
        if node.left and node.left.val >= node.val:
            flag = False
        if node.right and node.right.val <= node.val:
            flag = False
        leftSum, ok1 = self.helper(node.left)
        rightSum, ok2 = self.helper(node.right)
        flag &= (ok1 & ok2)
        if flag:
            self.result = max(self.result, leftSum + rightSum + node.val)
        return leftSum + rightSum + node.val, flag


if __name__ == '__main__':
    solution = Solution()

    # root = TreeNode(4)
    # root.left = TreeNode(3)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(2)
    # print(solution.maxSumBST(root))
    #
    # root = TreeNode(2)
    # root.left = TreeNode(1)
    # root.right = TreeNode(3)
    # print(solution.maxSumBST(root))

    root = TreeNode(-4)
    root.left = TreeNode(-2)
    root.right = TreeNode(-5)
    print(solution.maxSumBST(root))