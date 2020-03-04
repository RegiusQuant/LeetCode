# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 上午10:05
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0994.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n, queue, visit = len(grid), len(grid[0]), deque(), set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visit.add((i, j))

        result = 0
        while queue:
            cx, cy, t = queue.popleft()
            result = t
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in visit:
                    queue.append((nx, ny, t + 1))
                    visit.add((nx, ny))
                    grid[nx][ny] = 2

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    print(solution.orangesRotting([[0, 2]]))
