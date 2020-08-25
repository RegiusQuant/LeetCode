# -*- coding: utf-8 -*-
# @Time       : 2020/08/24 23:32:01
# @Author     : RegiusQuant <315135833@qq.com>
# @Project    : LeetCode
# @File       : 0529.py
# @Description: 文件说明

from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(cx, cy):
            count = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == dy == 0:
                        continue
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'M':
                        count += 1

            if count > 0:
                board[cx][cy] = str(count)
                return

            board[cx][cy] = 'B'
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == dy == 0:
                        continue
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'E':
                        dfs(nx, ny)

        cx, cy = click
        if board[cx][cy] == 'M':
            board[cx][cy] = 'X'
        else:
            dfs(cx, cy)
        return board


if __name__ == "__main__":
    solution = Solution()
    print(solution.updateBoard(
        [['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']],
        [3, 0]
    ))
