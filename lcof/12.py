# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 下午8:41
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 12.py
# @Desc    : 说明

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, x, y, word):
        if len(word) == 0:
            return True
        m, n = len(board), len(board[0])
        if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[0]:
            return False
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        board[x][y] = '*'
        for dx, dy in d:
            if self.dfs(board, x + dx, y + dy, word[1:]):
                return True
        board[x][y] = word[0]
        return False


if __name__ == '__main__':
    solution = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = 'ABCCED'
    print(solution.exist(board, word))
    board = [["a", "b"], ["c", "d"]]
    word = 'abcd'
    print(solution.exist(board, word))
