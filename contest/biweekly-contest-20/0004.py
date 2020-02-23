# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 下午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

class Solution:
    def countOrders(self, n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            a = 2 * (i - 1) + 1
            b = a * (a - 1) // 2 + a
            result = result * b % int(1e9 + 7)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countOrders(3))
