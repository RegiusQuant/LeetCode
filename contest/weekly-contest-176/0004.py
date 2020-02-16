# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 上午11:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        while sum(target) != len(target):
            maxVal, index = 0, -1
            for i in range(len(target)):
                if target[i] < 1:
                    return False
                if target[i] > maxVal:
                    maxVal = target[i]
                    index = i
            target[index] -= sum(target) - target[index]
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPossible([9, 3, 5]))
    print(solution.isPossible([1, 1, 1, 2]))
    print(solution.isPossible([8, 5]))
