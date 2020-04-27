# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 上午10:07
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0033.py
# @Desc    : 说明

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
