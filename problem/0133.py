# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 上午12:55
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0133.py
# @Desc    : 说明


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def __init__(self):
        self.visit = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visit:
            return self.visit[node]
        result = Node(node.val)
        self.visit[node] = result
        for v in node.neighbors:
            result.neighbors.append(self.cloneGraph(v))
        return result
