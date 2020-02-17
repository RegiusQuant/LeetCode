# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 下午8:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 11.py
# @Desc    : 说明

from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if len(numbers) < 3:
            return min(numbers)
        if numbers[0] < numbers[-1]:
            return numbers[0]

        pos = len(numbers) // 2
        if numbers[pos] > numbers[0]:
            return self.minArray(numbers[pos + 1:])
        elif numbers[pos] < numbers[0]:
            return self.minArray(numbers[:pos + 1])
        else:
            return min(self.minArray(numbers[pos + 1:]), self.minArray(numbers[:pos + 1]))


if __name__ == '__main__':
    solution = Solution()
    print(solution.minArray([3, 4, 5, 1, 2]))
    print(solution.minArray([2, 2, 2, 0, 1]))
