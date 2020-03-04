# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 上午10:17
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 53-2.py
# @Desc    : 说明

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right, result = 0, len(nums) - 1, len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left += 1
            else:
                right -= 1
                result = mid
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber([0, 1, 3]))
    print(solution.missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 9]))
