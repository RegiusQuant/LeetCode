# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 上午10:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List
from functools import lru_cache


class Solution:
    def __init__(self):
        self.total = 0
        self.valid = 0

    def getProbability(self, balls: List[int]) -> float:
        n, k = sum(balls) // 2, len(balls)

        @lru_cache(None)
        def calcFactorial(x):
            if x == 1:
                return 1
            return x * calcFactorial(x - 1)

        def calcTotalNum(arr):
            result = calcFactorial(sum(arr))
            for x in arr:
                if x > 1:
                    result //= calcFactorial(x)
            return result

        def dfs(left):
            if len(left) == k:
                if sum(left) == n:
                    right = [balls[i] - left[i] for i in range(k)]
                    count = calcTotalNum(left) * calcTotalNum(right)
                    self.total += count
                    # print(left, right, count)
                    c1, c2 = sum(left[i] > 0 for i in range(k)), sum(right[i] > 0 for i in range(k))
                    if c1 == c2:
                        self.valid += count
                return

            for i in range(min(balls[len(left)], n - sum(left)) + 1):
                left.append(i)
                dfs(left)
                left.pop()

        dfs([])
        # print(self.valid, self.total)
        return self.valid / self.total


if __name__ == '__main__':
    solution = Solution()
    print(solution.getProbability([1, 1]))
    solution = Solution()
    print(solution.getProbability([2, 1, 1]))
    solution = Solution()
    print(solution.getProbability([1, 2, 1, 2]))
    solution = Solution()
    print(solution.getProbability([3, 2, 1]))
    solution = Solution()
    print(solution.getProbability([6, 6, 6, 6, 6, 6]))