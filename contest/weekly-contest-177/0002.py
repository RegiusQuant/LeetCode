# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 上午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class UnionFind:

    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        self.root[y] = x
        return True


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = UnionFind(n)
        for i in range(n):
            left, right = leftChild[i], rightChild[i]
            if left != -1:
                if uf.find(left) != left or uf.find(left) == uf.find(i):
                    return False
                uf.union(i, left)
            if right != -1:
                if uf.find(right) != right or uf.find(right) == uf.find(i):
                    return False
                uf.union(i, right)
        return sum([1 for i in range(n) if uf.root[i] == i]) == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, -1, -1, -1]))
    print(solution.validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, 3, -1, -1]))
    print(solution.validateBinaryTreeNodes(2, [1, 0], [-1, -1]))
    print(solution.validateBinaryTreeNodes(6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1]))
