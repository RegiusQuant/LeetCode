# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 上午9:17
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.py
# @Desc    : 说明

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1. / x, -n)
        else:
            tmp = self.myPow(x, n // 2)
            tmp *= tmp
            if n % 2:
                tmp *= x
            return tmp


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2.0, 10))
    print(solution.myPow(2.1, 3))
    print(solution.myPow(2.0, -2))
