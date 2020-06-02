# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 上午9:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0079.py
# @Desc    : 说明

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        if not word:
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and self.dfs(i, j, 0, board, word):
                    return True
        return False

    def dfs(self, i, j, idx, board, word):
        idx = idx + 1
        if idx == len(word):
            return True

        direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
        m, n = len(board), len(board[0])

        tmp, board[i][j] = board[i][j], '@'
        for k in range(4):
            x, y = i + direction[k][0], j + direction[k][1]
            if 0 <= x < m and 0 <= y < n and board[x][y] == word[idx]:
                if self.dfs(x, y, idx, board, word):
                    return True
        board[i][j] = tmp
        return False
