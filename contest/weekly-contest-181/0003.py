# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 下午2:06
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def __init__(self):

        self.direction = {
            1: [(0, -1, (1, 4, 6)), (0, 1, (1, 3, 5))],
            2: [(-1, 0, (2, 3, 4)), (1, 0, (2, 5, 6))],
            3: [(0, -1, (1, 4, 6)), (1, 0, (2, 5, 6))],
            4: [(0, 1, (1, 3, 5)), (1, 0, (2, 5, 6))],
            5: [(0, -1, (1, 4, 6)), (-1, 0, (2, 3, 4))],
            6: [(0, 1, (1, 3, 5)), (-1, 0, (2, 3, 4))],
        }

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        while queue:
            cx, cy = queue.popleft()
            if cx == m - 1 and cy == n - 1:
                return True
            for dx, dy, t in self.direction[grid[cx][cy]]:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx, ny) in visit:
                    continue
                if grid[nx][ny] not in t:
                    continue
                queue.append((nx, ny))
                visit.add((nx, ny))
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.hasValidPath(grid=[[2, 4, 3], [6, 5, 2]]))
    print(solution.hasValidPath(grid=[[1, 2, 1], [1, 2, 1]]))
    print(solution.hasValidPath(grid=[[1, 1, 2]]))
    print(solution.hasValidPath(grid=[[1, 1, 1, 1, 1, 1, 3]]))
    print(solution.hasValidPath(grid=[[2], [2], [2], [2], [2], [2], [6]]))
