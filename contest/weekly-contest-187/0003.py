# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 上午10:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxVals, minVals = deque(), deque()
        left, right = 0, 0

        result = 0
        while right < len(nums):
            while maxVals and maxVals[-1] < nums[right]:
                maxVals.pop()
            maxVals.append(nums[right])

            while minVals and minVals[-1] > nums[right]:
                minVals.pop()
            minVals.append(nums[right])

            while maxVals[0] - minVals[0] > limit:
                if maxVals[0] == nums[left]:
                    maxVals.popleft()
                if minVals[0] == nums[left]:
                    minVals.popleft()
                left += 1
            result = max(result, right - left + 1)
            right += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestSubarray([8, 2, 4, 7], 4))
    print(solution.longestSubarray([10, 1, 2, 4, 7, 2], 5))
    print(solution.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))
