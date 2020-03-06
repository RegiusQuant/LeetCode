# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 上午9:46
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 57-2.py
# @Desc    : 说明

import math
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        result = []
        for i in range(1, target // 2 + 1):
            c = -(2 * target + i ** 2 - i)
            t = int(math.sqrt(1 - 4 * c))
            if t * t == 1 - 4 * c and (t - 1) % 2 == 0:
                result.append(list(range(i, (t - 1) // 2 + 1)))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findContinuousSequence(9))
