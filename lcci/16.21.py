# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 上午11:06
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.21.py
# @Desc    : 说明

from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum1, sum2 = sum(array1), sum(array2)
        if (sum2 - sum1) % 2:
            return []
        diff = (sum2 - sum1) // 2
        s = set(array2)

        for x in array1:
            if x + diff in s:
                return [x, x + diff]
        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSwapValues(array1=[4, 1, 2, 1, 1, 2], array2=[3, 6, 3, 3]))
    print(solution.findSwapValues(array1=[1, 2, 3], array2=[4, 5, 6]))
