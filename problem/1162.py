# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 下午12:44
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1162.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        visit, queue = set(), deque()
        dist = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visit.add((i, j))
                else:
                    dist[i][j] = float('inf')

        while queue:
            cx, cy = queue.popleft()
            visit.remove((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx, ny) in visit:
                    continue
                if grid[nx][ny] == 1:
                    continue
                if dist[nx][ny] > dist[cx][cy] + 1:
                    dist[nx][ny] = dist[cx][cy] + 1
                    queue.append((nx, ny))
                    visit.add((nx, ny))

        result = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    result = max(result, dist[i][j])

        return result if result != float('inf') else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDistance(
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    ))
    print(solution.maxDistance(
        [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    ))
