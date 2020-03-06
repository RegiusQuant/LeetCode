# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 上午10:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 57.py
# @Desc    : 说明

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result, left, right = [], 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                result.extend([nums[left], nums[right]])
                break
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
