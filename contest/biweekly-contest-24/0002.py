# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 下午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while True:
            fib.append(fib[-1] + fib[-2])
            if fib[-1] > int(1e9):
                break
        result, p = 0, len(fib) - 1
        while k:
            while fib[p] > k:
                p -= 1
            k -= fib[p]
            result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMinFibonacciNumbers(7))
    print(solution.findMinFibonacciNumbers(2))
    print(solution.findMinFibonacciNumbers(19))
