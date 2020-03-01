# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 上午10:08
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:

    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        direction = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        dist = [[m + n] * n for _ in range(m)]
        visit = [[False] * n for _ in range(m)]

        queue = deque()
        queue.append((0, 0))
        visit[0][0] = True
        dist[0][0] = 0

        while queue:
            cx, cy = queue.popleft()
            visit[cx][cy] = False

            for i, (dx, dy) in direction.items():
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nt = dist[cx][cy] if grid[cx][cy] == i else dist[cx][cy] + 1
                    if nt < dist[nx][ny]:
                        dist[nx][ny] = nt
                        if not visit[nx][ny]:
                            queue.append((nx, ny))
                            visit[nx][ny] = True

        return dist[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))
    print(solution.minCost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]))
    print(solution.minCost([[1, 2], [4, 3]]))
    print(solution.minCost([[2, 2, 2], [2, 2, 2]]))
    print(solution.minCost([[4]]))
