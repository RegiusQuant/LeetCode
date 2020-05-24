# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 上午10:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        counter = Counter()
        self.helper(root, counter)
        return self.result

    def helper(self, root: TreeNode, counter: Counter):
        counter[root.val] += 1
        if not root.left and not root.right:
            odd = 0
            for v in counter.values():
                if v % 2 == 1:
                    odd += 1
            if odd <= 1:
                self.result += 1
            counter[root.val] -= 1
            return

        if root.left:
            self.helper(root.left, counter)
        if root.right:
            self.helper(root.right, counter)
        counter[root.val] -= 1


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right = TreeNode(1)
    root.right.right = TreeNode(1)
    print(solution.pseudoPalindromicPaths(root))