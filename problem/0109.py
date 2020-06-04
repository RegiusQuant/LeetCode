# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 上午9:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0109.py
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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        prev, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        node = TreeNode(slow.val)
        prev.next = None
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node


if __name__ == '__main__':
    solution = Solution()
