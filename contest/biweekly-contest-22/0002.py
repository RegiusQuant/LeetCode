# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(list)
        for x, y in reservedSeats:
            seats[x].append(y)

        result = 0
        for k in seats.keys():
            seat = [0] * 10
            for v in seats[k]:
                seat[v - 1] = 1
            temp = 0
            for v in [1, 3, 5]:
                if sum(seat[v:v + 4]) == 0:
                    temp += 1
                    seat[v:v + 4] = [1] * 4
            result += temp
        result += (n - len(seats)) * 2
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxNumberOfFamilies(3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
    print(solution.maxNumberOfFamilies(2, [[2, 1], [1, 8], [2, 6]]))
    print(solution.maxNumberOfFamilies(4, [[4, 3], [1, 4], [4, 6], [1, 7]]))
