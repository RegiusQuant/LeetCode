# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 上午10:13
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 56-2.py
# @Desc    : 说明

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            c, b = 0, 1 << i
            for x in nums:
                if x & b != 0:
                    c += 1
            if c % 3 != 0:
                result |= b
        return result - 2 ** 32 if result > 2 ** 31 - 1 else result


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([3, 4, 3, 3]))
    print(solution.singleNumber([9, 1, 7, 9, 7, 9, 7]))
