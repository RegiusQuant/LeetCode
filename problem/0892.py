# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 上午10:06
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0892.py
# @Desc    : 说明

from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n, result = len(grid), 0
        for i in range(n):
            for j in range(n):
                result += max(0, grid[i][j] - grid[i - 1][j]) if i > 0 else grid[i][j]
                result += max(0, grid[i][j] - grid[i + 1][j]) if i < n - 1 else grid[i][j]
                result += max(0, grid[i][j] - grid[i][j - 1]) if j > 0 else grid[i][j]
                result += max(0, grid[i][j] - grid[i][j + 1]) if j < n - 1 else grid[i][j]
                result += 2 if grid[i][j] > 0 else 0
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.surfaceArea([[2]]))
    print(solution.surfaceArea([[1, 2], [3, 4]]))
    print(solution.surfaceArea([[1, 0], [0, 2]]))
    print(solution.surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(solution.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
