# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 上午10:30
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        result, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    result += n - j
                    break
        return result


if __name__ == '__main__':
    solution = Solution()
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(solution.countNegatives(grid))
    grid = [[3, 2], [1, 0]]
    print(solution.countNegatives(grid))
    grid = [[-1]]
    print(solution.countNegatives(grid))
