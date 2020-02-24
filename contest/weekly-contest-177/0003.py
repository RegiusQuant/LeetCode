# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 上午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

import math
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        r1 = self.helper(num + 1)
        r2 = self.helper(num + 2)
        if abs(r1[0] - r1[1]) < abs(r2[0] - r2[1]):
            return r1
        else:
            return r2

    def helper(self, num: int) -> List[int]:
        result = [1, num]
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                result = [i, num // i]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.closestDivisors(8))
    print(solution.closestDivisors(123))
    print(solution.closestDivisors(999))
