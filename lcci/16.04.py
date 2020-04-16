# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 上午10:26
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.04.py
# @Desc    : 说明

from typing import List


class Solution:
    def tictactoe(self, board: List[str]) -> str:
        if self.checkWin(board, 'X'):
            return 'X'
        if self.checkWin(board, 'O'):
            return 'O'
        if self.checkFin(board):
            return 'Draw'
        return 'Pending'

    def checkWin(self, board, x):
        n = len(board)
        for k in range(n):
            count = sum(1 for i in range(n) if board[k][i] == x)
            if count == n:
                return True
            count = sum(1 for i in range(n) if board[i][k] == x)
            if count == n:
                return True

        count = sum(1 for i in range(n) if board[i][i] == x)
        if count == n:
            return True
        count = sum(1 for i in range(n) if board[i][n - i - 1] == x)
        if count == n:
            return True
        return False

    def checkFin(self, board):
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == ' ':
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.tictactoe(
        ["O X", " XO", "X O"]
    ))
    print(solution.tictactoe(
        ["OOX", "XXO", "OXO"]
    ))
    print(solution.tictactoe(
        ["OOX", "XXO", "OX "]
    ))
    print(solution.tictactoe(
        ["O"]
    ))