# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 下午6:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0695.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result = max(result, self.bfs(i, j, m, n, grid))
        return result

    def bfs(self, x, y, m, n, grid):
        queue = deque()
        queue.append((x, y))
        grid[x][y], count = 0, 1

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                tx, ty = cx + dx, cy + dy
                if 0 <= tx < m and 0 <= ty < n and grid[tx][ty] == 1:
                    queue.append((tx, ty))
                    grid[tx][ty] = 0
                    count += 1
        return count
