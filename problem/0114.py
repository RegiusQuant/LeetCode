# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 下午9:30
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0114.py
# @Desc    : 说明


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                pre = nxt = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.left = None
                cur.right = nxt
            cur = cur.right
