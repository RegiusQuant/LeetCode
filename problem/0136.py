# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 上午10:41
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0136.py
# @Desc    : 说明

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            result ^= x
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([2, 2, 1]))
    print(solution.singleNumber([4, 1, 2, 1, 2]))
