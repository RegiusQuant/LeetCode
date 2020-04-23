# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 上午10:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.16.py
# @Desc    : 说明

from typing import List


class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        start, end = -1, -1
        maxVal, minVal = float('-inf'), float('inf')
        for i in range(len(array)):
            if array[i] < maxVal:
                end = i
            else:
                maxVal = array[i]
            if array[len(array) - i - 1] > minVal:
                start = len(array) - i - 1
            else:
                minVal = array[len(array) - i - 1]
        return [start, end]


if __name__ == '__main__':
    solution = Solution()
    print(solution.subSort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
