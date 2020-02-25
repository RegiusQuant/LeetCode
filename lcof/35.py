# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 上午11:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 35.py
# @Desc    : 说明


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visit = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        result = self.helper(head)
        return result

    def helper(self, oldNode: 'Node') -> 'Node':
        if not oldNode:
            return None
        if oldNode in self.visit:
            return self.visit[oldNode]
        newNode = Node(oldNode.val)
        self.visit[oldNode] = newNode
        newNode.next = self.helper(oldNode.next)
        newNode.random = self.helper(oldNode.random)
        return newNode
