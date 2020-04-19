# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 下午2:15
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from functools import lru_cache


class Solution:

    @lru_cache(None)
    def helper(self, n: int, m: int, k: int) -> int:
        if n == 0 or k == 0 or m == 0:
            return 0
        if n == 1 and k == 1:
            return 1

        result = 0
        for i in range(1, m):
            result = (result + self.helper(n - 1, i, k - 1)) % int(1e9 + 7)
        result = (result + self.helper(n - 1, m, k) * m) % int(1e9 + 7)
        return result

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        result = 0
        for i in range(1, m + 1):
            result = (result + self.helper(n, i, k)) % int(1e9 + 7)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numOfArrays(2, 3, 1))
    print(solution.numOfArrays(5, 2, 3))
    print(solution.numOfArrays(9, 1, 1))
    print(solution.numOfArrays(50, 100, 25))
