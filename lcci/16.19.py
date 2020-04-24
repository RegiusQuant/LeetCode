# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 上午10:58
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.19.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])
        visit = set()
        result = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0 and (i, j) not in visit:
                    result.append(self.bfs(i, j, m, n, land, visit))
        return sorted(result)

    def bfs(self, x, y, m, n, land, visit):
        result = 1
        queue = deque([(x, y)])
        visit.add((x, y))
        while queue:
            cx, cy = queue.popleft()
            for nx, ny in [(cx - 1, cy - 1), (cx - 1, cy), (cx - 1, cy + 1),
                           (cx, cy - 1), (cx, cy + 1),
                           (cx + 1, cy - 1), (cx + 1, cy), (cx + 1, cy + 1)]:
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visit and land[nx][ny] == 0:
                    queue.append((nx, ny))
                    visit.add((nx, ny))
                    result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.pondSizes([
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]))
