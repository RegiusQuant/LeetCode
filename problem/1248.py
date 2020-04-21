# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 下午1:39
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1248.py
# @Desc    : 说明

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n, result = len(nums), 0
        odd = [-1] + [i for i, x in enumerate(nums) if x % 2] + [n]
        for i in range(1, len(odd) - k):
            result += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
    print(solution.numberOfSubarrays(nums=[2, 4, 6], k=1))
    print(solution.numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))
