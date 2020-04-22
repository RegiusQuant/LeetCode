# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 上午11:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.14.py
# @Desc    : 说明

from typing import List


class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        maxLine = 0
        result = [0, 1]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                temp = 0
                for k in range(j + 1, len(points)):
                    t1 = [points[k][0] - points[i][0], points[k][1] - points[i][1]]
                    t2 = [points[j][0] - points[i][0], points[j][1] - points[i][1]]
                    if t2[1] * t1[0] == t2[0] * t1[1]:
                        temp += 1
                if temp > maxLine:
                    maxLine = temp
                    result = [i, j]
        return result
