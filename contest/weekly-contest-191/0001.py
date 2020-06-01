# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 上午10:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                result = max(result, (nums[i] - 1) * (nums[j] - 1))
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([3, 4, 5, 2]))
    print(solution.maxProduct([1, 5, 4, 5]))
    print(solution.maxProduct([3, 7]))
