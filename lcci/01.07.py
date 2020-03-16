# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 上午10:21
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 01.07.py
# @Desc    : 说明

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = list(map(list, zip(*matrix[::-1])))


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    solution.rotate(matrix)
    print(matrix)
