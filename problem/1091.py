# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 上午9:24
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1091.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        m, n = len(grid), len(grid[0])
        dist = {(0, 0): 1}
        queue = deque([(0, 0, 1)])
        while queue:
            cx, cy, cd = queue.popleft()
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in dist:
                        queue.append((nx, ny, cd + 1))
                        dist[(nx, ny)] = cd + 1

        if (m - 1, n - 1) not in dist:
            return -1
        return dist[(m - 1, n - 1)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
    print(solution.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
