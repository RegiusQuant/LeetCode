# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 下午2:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 21.py
# @Desc    : 说明

from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] % 2 == 0:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1
        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.exchange([1, 2, 3, 4]))
