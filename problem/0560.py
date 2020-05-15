# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 上午10:50
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0560.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter()
        counter[0] = 1
        total, result = 0, 0
        for x in nums:
            total += x
            result += counter[total - k]
            counter[total] += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))
