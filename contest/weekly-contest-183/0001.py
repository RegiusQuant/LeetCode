# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 上午10:18
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        nums.sort(reverse=True)
        result = []
        for i in range(len(nums)):
            result.append(nums[i])
            total -= nums[i]
            if sum(result) > total:
                return result
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubsequence([4, 3, 10, 9, 8]))
    print(solution.minSubsequence([4, 4, 7, 6, 7]))
    print(solution.minSubsequence([6]))
