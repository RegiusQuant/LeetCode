# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 上午10:45
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 47.py
# @Desc    : 说明

from typing import List


class Solution:

    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                currVal, prevVal = grid[i][j], 0
                if i > 0:
                    prevVal = max(prevVal, grid[i - 1][j])
                if j > 0:
                    prevVal = max(prevVal, grid[i][j - 1])
                grid[i][j] = currVal + prevVal
        return grid[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxValue([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1],
    ]))
