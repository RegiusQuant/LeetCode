# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 下午2:05
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0365.py
# @Desc    : 说明

import math


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.canMeasureWater(3, 5, 4))
    print(solution.canMeasureWater(2, 6, 5))
