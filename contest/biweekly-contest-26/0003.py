# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root, root.val)
        return self.result

    def helper(self, node: TreeNode, maxVal: int):
        if not node:
            return

        if node.val >= maxVal:
            self.result += 1
        self.helper(node.left, max(maxVal, node.val))
        self.helper(node.right, max(maxVal, node.val))


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    solution = Solution()
    print(solution.goodNodes(root))

    root = TreeNode(3)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(2)
    solution = Solution()
    print(solution.goodNodes(root))

    root = TreeNode(1)
    solution = Solution()
    print(solution.goodNodes(root))