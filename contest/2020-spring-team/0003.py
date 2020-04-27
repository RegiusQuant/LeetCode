# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 上午10:16
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List
from copy import deepcopy
from collections import deque


class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        m, n = len(maze), len(maze[0])
        start, end = None, None
        keys, locks = [], []

        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'S':
                    start = (i, j)
                elif maze[i][j] == 'T':
                    end = (i, j)
                elif maze[i][j] == 'O':
                    keys.append((i, j))
                elif maze[i][j] == 'M':
                    locks.append((i, j))

        locks.insert(0, start)
        nkey, nlock = len(keys), len(locks)
        tdist = [[float('inf')] * n for _ in range(m)]
        kdist = [deepcopy(tdist) for _ in range(nkey)]

        def bfs(sx, sy, dist):
            queue = deque()
            queue.append((sx, sy))
            visit = set()
            visit.add((sx, sy))
            dist[sx][sy] = 0

            while queue:
                cx, cy = queue.popleft()
                for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visit and maze[nx][ny] != '#':
                        dist[nx][ny] = dist[cx][cy] + 1
                        queue.append((nx, ny))
                        visit.add((nx, ny))

        for i in range(nkey):
            bfs(keys[i][0], keys[i][1], kdist[i])
        bfs(end[0], end[1], tdist)
        # print(tdist)

        ldist = [[float('inf')] * nlock for _ in range(nlock)]
        for i in range(nlock):
            for j in range(nlock):
                if i == j:
                    continue
                for k in range(nkey):
                    ldist[i][j] = min(
                        ldist[i][j],
                        kdist[k][locks[i][0]][locks[i][1]] + kdist[k][locks[j][0]][locks[j][1]]
                    )
        # print(ldist)

        dp = [[float('inf')] * (1 << nlock) for _ in range(nlock)]
        dp[0][1] = 0
        for state in range(1, (1 << nlock)):
            for curr in range(nlock):
                if dp[curr][state] == float('inf'):
                    continue
                for i in range(1, nlock):
                    if state & (1 << i):
                        continue
                    nxt = (state + (1 << i))
                    dp[i][nxt] = min(dp[i][nxt], dp[curr][state] + ldist[curr][i])
        # print(dp)

        result = float('inf')
        for i in range(nlock):
            result = min(result, dp[i][-1] + tdist[locks[i][0]][locks[i][1]])
        if result == float('inf'):
            return -1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimalSteps(["S#O", "M..", "M.T"]))
    print(solution.minimalSteps(["S#O", "M.#", "M.T"]))
    print(solution.minimalSteps(["S#O", "M.T", "M.."]))
