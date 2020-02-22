# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 上午10:47
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 29.py
# @Desc    : 说明

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return result


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.spiralOrder(matrix))
