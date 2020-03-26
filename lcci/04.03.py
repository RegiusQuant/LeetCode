# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 上午10:40
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 04.03.py
# @Desc    : 说明

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.result = []
        self.temp = []

    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        self.helper(tree, 0)
        return self.result

    def helper(self, node: TreeNode, dep: int):
        if not node:
            return
        if dep == len(self.result):
            t = ListNode(node.val)
            self.result.append(t)
            self.temp.append(t)
        else:
            self.temp[dep].next = ListNode(node.val)
            self.temp[dep] = self.temp[dep].next
        self.helper(node.left, dep + 1)
        self.helper(node.right, dep + 1)


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    solution = Solution()
    print(solution.listOfDepth(tree))
