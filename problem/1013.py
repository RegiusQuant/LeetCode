# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 上午9:43
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1013.py
# @Desc    : 说明

from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3:
            return False
        leftSum, rightSum = 0, 0
        leftPos, rightPos = -1, -1
        for i in range(len(A)):
            leftSum += A[i]
            if leftSum == total // 3:
                leftPos = i
                break
        for i in range(len(A) - 1, -1, -1):
            rightSum += A[i]
            if rightSum == total // 3:
                rightPos = i
                break
        return leftPos + 1 < rightPos


if __name__ == '__main__':
    solution = Solution()
    print(solution.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
    print(solution.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
    print(solution.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
    print(solution.canThreePartsEqualSum([1, -1, 1, -1]))