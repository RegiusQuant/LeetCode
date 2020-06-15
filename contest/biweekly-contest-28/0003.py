# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 下午9:59
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        temp, d, s = [], {0: 0}, 0
        for i in range(len(arr)):
            s += arr[i]
            if s - target in d:
                temp.append((d[s - target], i + 1))
            d[s] = i + 1
        if len(temp) <= 1:
            return -1
        temp.sort(key=lambda x: x[1] - x[0])
        for i in range(len(temp)):
            for j in range(i + 1, len(temp)):
                if temp[i][0] < temp[j][0] < temp[i][1]:
                    continue
                return temp[i][1] - temp[i][0] + temp[j][1] - temp[j][0]
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSumOfLengths([3, 2, 2, 4, 3], 3))
    print(solution.minSumOfLengths([7, 3, 4, 7], 7))
    print(solution.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6))
    print(solution.minSumOfLengths([5, 5, 4, 4, 5], 3))
    print(solution.minSumOfLengths([3, 1, 1, 1, 5, 1, 2, 1], 3))
    print(solution.minSumOfLengths([1, 6, 1], 7))
    print(solution.minSumOfLengths([1, 6, 1], 7))
    print(solution.minSumOfLengths([64, 5, 20, 9, 1, 39], 69))
