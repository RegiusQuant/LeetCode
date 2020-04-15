# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 下午1:16
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0542.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        start = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        queue = deque(start)
        visit = set(start)

        while queue:
            cx, cy = queue.popleft()
            for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visit:
                    dist[nx][ny] = dist[cx][cy] + 1
                    queue.append((nx, ny))
                    visit.add((nx, ny))
        return dist


if __name__ == '__main__':
    solution = Solution()
    print(solution.updateMatrix([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
