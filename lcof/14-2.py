# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 上午10:17
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 14-2.py
# @Desc    : 说明

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1

        result = 0
        if n % 3 == 0:
            result = 1
        elif n % 3 == 1:
            result = 4
            n -= 4
        else:
            result = 2
            n -= 2
        for i in range(n // 3):
            result = (result * 3) % int(1e9 + 7)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.cuttingRope(2))
    print(solution.cuttingRope(10))
