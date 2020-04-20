# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 上午10:05
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0200.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        visit = [[False] * n for _ in range(m)]

        result = 0
        for i in range(m):
            for j in range(n):
                if not visit[i][j] and grid[i][j] == '1':
                    result += 1
                    self.bfs(i, j, grid, visit)
        return result

    def bfs(self, x, y, grid, visit):
        m, n = len(grid), len(grid[0])
        queue = deque()
        queue.append((x, y))
        visit[x][y] = True

        while queue:
            cx, cy = queue.popleft()
            for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
                if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny] and grid[nx][ny] == '1':
                    queue.append((nx, ny))
                    visit[nx][ny] = True


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands([
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]))
