# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 下午7:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0138.py
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

    def helper(self, node: 'Node') -> 'Node':
        if not node:
            return None

        if node in self.visit:
            return self.visit[node]

        newNode = Node(node.val)
        self.visit[node] = newNode
        newNode.next = self.helper(node.next)
        newNode.random = self.helper(node.random)
        return newNode
