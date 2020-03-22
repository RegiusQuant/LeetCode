# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 下午1:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

import math
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            count, temp = 0, 0
            for i in range(1, int(math.sqrt(x) + 1)):
                if x % i == 0:
                    if i * i == x:
                        temp += i
                        count += 1
                    else:
                        temp += (x // i) + i
                        count += 2
                    if count > 4:
                        break
            result += temp if count == 4 else 0
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumFourDivisors([21, 4, 7]))
