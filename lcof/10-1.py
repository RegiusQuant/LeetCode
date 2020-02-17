# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 下午8:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 10-1.py
# @Desc    : 说明

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, (a + b) % int(1e9 + 7)
        return b


if __name__ == '__main__':
    solution = Solution()
    print(solution.fib(2))
    print(solution.fib(5))
    print(solution.fib(100))
