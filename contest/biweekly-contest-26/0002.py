# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

import math
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if math.gcd(i, j) == 1:
                    result.append(str(j) + '/' + str(i))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.simplifiedFractions(2))
    print(solution.simplifiedFractions(3))
    print(solution.simplifiedFractions(4))
    print(solution.simplifiedFractions(1))
    print(solution.simplifiedFractions(100))