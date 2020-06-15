# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 下午2:21
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.dp = [[] for _ in range(n)]
        for i in range(n):
            self.dp[i].append(parent[i])

        depth = 1
        while True:
            flag = True
            for i in range(n):
                t = self.dp[self.dp[i][depth - 1]][depth - 1] if self.dp[i][depth - 1] != -1 else -1
                self.dp[i].append(t)
                if t != -1:
                    flag = False
            depth += 1
            if flag:
                break

    def getKthAncestor(self, node: int, k: int) -> int:
        result, pos = node, 0
        while k != 0 and result != -1:
            if pos >= len(self.dp[result]):
                return -1
            if k & 1:
                result = self.dp[result][pos]
            k //= 2
            pos += 1
        return result


if __name__ == '__main__':
    obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print(obj.getKthAncestor(3, 1))
    print(obj.getKthAncestor(5, 2))
    print(obj.getKthAncestor(6, 3))
