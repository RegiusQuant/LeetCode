# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 下午10:59
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0063.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or len(obstacleGrid[0]) == 0:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1 if not obstacleGrid[0][0] else 0
        visit = {(0, 0)}
        queue = deque()
        queue.append((0, 0))

        while queue:
            cx, cy = queue.popleft()
            for nx, ny in [(cx + 1, cy), (cx, cy + 1)]:
                if 0 <= nx < m and 0 <= ny < n and obstacleGrid[nx][ny] != 1:

                    dp[nx][ny] += dp[cx][cy]
                    if (nx, ny) not in visit:
                        visit.add((nx, ny))
                        queue.append((nx, ny))
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
    print(solution.uniquePathsWithObstacles([[1]]))