# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 下午8:15
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0050.py
# @Desc    : 说明

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n // 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2, -2147483648))
