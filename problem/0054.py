# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 上午10:51
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0054.py
# @Desc    : 说明

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result.extend(matrix[0])
            matrix = list(zip(*matrix[1:]))[::-1]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
