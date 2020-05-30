# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 下午8:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List
from functools import lru_cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(x, y1, y2):
            if y1 < 0 or y1 >= n or y2 < 0 or y2 >= n:
                return -10 ** 9

            if x == 0:
                if y1 == 0 and y2 == n - 1:
                    return grid[0][y1] + grid[0][y2]
                else:
                    return -10 ** 9

            temp = -10 ** 9
            for d1 in [-1, 0, 1]:
                for d2 in [-1, 0, 1]:
                    temp = max(temp, dfs(x - 1, y1 + d1, y2 + d2))
            if y1 != y2:
                temp += grid[x][y1] + grid[x][y2]
            else:
                temp += grid[x][y1]
            return temp

        result = 0
        for i in range(n):
            for j in range(n):
                result = max(result, dfs(m - 1, i, j))
                # print(i, j, result)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
    print(solution.cherryPickup([
        [1, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 3, 0],
        [2, 0, 9, 0, 0, 0, 0],
        [0, 3, 0, 5, 4, 0, 0],
        [1, 0, 2, 3, 0, 0, 6]
    ]))
    print(solution.cherryPickup([[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]))
    print(solution.cherryPickup([[1, 1], [1, 1]]))
    print(solution.cherryPickup(
        [[0, 8, 7, 10, 9, 10, 0, 9, 6],
         [8, 7, 10, 8, 7, 4, 9, 6, 10],
         [8, 1, 1, 5, 1, 5, 5, 1, 2],
         [9, 4, 10, 8, 8, 1, 9, 5, 0],
         [4, 3, 6, 10, 9, 2, 4, 8, 10],
         [7, 3, 2, 8, 3, 3, 5, 9, 8],
         [1, 2, 6, 5, 6, 2, 0, 10, 0]]
    ))
    print(solution.cherryPickup(
        [[1, 0, 1],
         [1, 10, 1],
         [1, 0, 1]]
    ))