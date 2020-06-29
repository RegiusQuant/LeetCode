# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 下午12:54
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0215.py
# @Desc    : 说明

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x > pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        if k <= len(left):
            return self.findKthLargest(left, k)
        elif k > len(left) + len(middle):
            return self.findKthLargest(right, k - len(left) - len(middle))
        else:
            return middle[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
