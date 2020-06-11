# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 上午9:46
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0739.py
# @Desc    : 说明

from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and T[i] > T[stack[-1]]:
                pos = stack.pop()
                result[pos] = i - pos
            stack.append(i)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
