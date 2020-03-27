# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 上午10:26
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0914.py
# @Desc    : 说明

import math
from collections import Counter
from typing import List
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return reduce(math.gcd, Counter(deck).values()) != 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
    print(solution.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
    print(solution.hasGroupsSizeX([1]))
    print(solution.hasGroupsSizeX([1, 1]))
    print(solution.hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
