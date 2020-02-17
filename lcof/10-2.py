# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 下午8:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 10-2.py
# @Desc    : 说明

class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, (a + b) % int(1e9 + 7)
        return b


if __name__ == '__main__':
    solution = Solution()
    print(solution.numWays(2))
    print(solution.numWays(7))
    print(solution.numWays(100))
