# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 上午10:08
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        if self.dfs(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, head: ListNode, root: TreeNode):
        if not head:
            return True
        if not root or head.val != root.val:
            return False
        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)
