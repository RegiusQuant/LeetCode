# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 下午1:04
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0945.py
# @Desc    : 说明

from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        result, pos = 0, 0
        for i in range(1, len(A)):
            d = i - pos
            if A[i] - A[pos] < d:
                result += d - (A[i] - A[pos])
            else:
                pos = i
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minIncrementForUnique([1, 2, 2]))
    print(solution.minIncrementForUnique([3, 2, 1, 2, 1, 7]))
