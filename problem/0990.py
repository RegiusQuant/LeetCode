# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 上午9:06
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0990.py
# @Desc    : 说明

from typing import List


class UnionFind:

    def __init__(self, n):
        self.root = [x for x in range(n)]

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            self.root[a] = b


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for s in equations:
            x = ord(s[0]) - ord('a')
            y = ord(s[-1]) - ord('a')
            if s[1] == '=':
                uf.union(x, y)
        for s in equations:
            x = ord(s[0]) - ord('a')
            y = ord(s[-1]) - ord('a')
            if s[1] == '!' and uf.find(x) == uf.find(y):
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.equationsPossible(["a==b", "b!=a"]))
    print(solution.equationsPossible(["b==a", "a==b"]))
    print(solution.equationsPossible(["a==b", "b==c", "a==c"]))
    print(solution.equationsPossible(["a==b", "b!=c", "c==a"]))
    print(solution.equationsPossible(["c==c", "b==d", "x!=z"]))
