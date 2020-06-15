# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 下午9:59
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.data = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.data[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.data[row][col]


if __name__ == '__main__':
    obj = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    print(obj.getValue(0, 2))
