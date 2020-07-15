# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 下午9:41
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0120.py
# @Desc    : 说明

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        record = triangle[-1]
        for k in range(len(triangle) - 2, -1, -1):
            temp = []
            for i in range(len(triangle[k])):
                temp.append(min(record[i], record[i + 1]) + triangle[k][i])
            record = temp
        return record[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
