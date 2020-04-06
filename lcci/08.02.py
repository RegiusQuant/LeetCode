# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 上午10:53
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.02.py
# @Desc    : 说明

from typing import List
from copy import deepcopy


class Solution:
    def __init__(self):
        self.result = []
        self.visit = set()

    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 0:
            self.helper(0, 0, m, n, obstacleGrid, [])
        return self.result

    def helper(self, cx, cy, m, n, grid, path):
        if self.result:
            return

        path.append([cx, cy])
        self.visit.add((cx, cy))
        if cx == m - 1 and cy == n - 1:
            self.result = deepcopy(path)

        for dx, dy in [(0, 1), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in self.visit and grid[nx][ny] != 1:
                self.helper(nx, ny, m, n, grid, path)
        path.pop()


if __name__ == '__main__':
    solution = Solution()
    print(solution.pathWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
    solution = Solution()
    print(solution.pathWithObstacles([
        [0, 1]
    ]))
