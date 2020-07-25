# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 下午10:07
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0039.py
# @Desc    : 说明

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right, result = 0, len(nums) - 1, 0
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                result = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 5))
    print(solution.searchInsert([1, 3, 5, 6], 2))
    print(solution.searchInsert([1, 3, 5, 6], 7))
    print(solution.searchInsert([1, 3, 5, 6], 0))