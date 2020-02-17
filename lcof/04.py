# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 下午6:26
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 04.py
# @Desc    : 说明

from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        x, y = len(matrix) - 1, 0
        while x >= 0 and y < len(matrix[0]):
            if target < matrix[x][y]:
                x -= 1
            elif target > matrix[x][y]:
                y += 1
            else:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(solution.findNumberIn2DArray(matrix, 5))
    print(solution.findNumberIn2DArray(matrix, 20))
