# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 上午11:26
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0572.py
# @Desc    : 说明

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.check(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def check(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)


if __name__ == '__main__':
    s = TreeNode(1)
    s.left = TreeNode(1)
    s.left.left = TreeNode(1)
    s.left.left.left = TreeNode(1)
    s.left.left.right = TreeNode(2)
    t = s.left.left
    solution = Solution()
    print(solution.isSubtree(s, t))
