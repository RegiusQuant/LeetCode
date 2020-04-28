# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 上午10:52
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.24.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        counter = Counter(nums)

        for x in nums:
            y = target - x
            if x != y and counter[x] > 0 and counter[y] > 0:
                result.append([x, y])
                counter[x] -= 1
                counter[y] -= 1
            if x == y and counter[x] >= 2:
                result.append([x, x])
                counter[x] -= 2
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.pairSums([5, 6, 5], 11))
    print(solution.pairSums([5, 6, 5, 6], 11))
