# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午1:35
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        if 3 ** int(math.log(n, 3) + 1e-7) == n:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfThree(27))
    print(solution.isPowerOfThree(0))
    print(solution.isPowerOfThree(9))
    print(solution.isPowerOfThree(45))
    print(solution.isPowerOfThree(243))