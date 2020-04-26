# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 下午2:46
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        queue = deque()
        queue.append((dp[0], 0))

        for i in range(1, len(nums)):
            while queue and i - queue[0][1] > k:
                queue.popleft()

            dp[i] = max(0, queue[0][0]) + nums[i]

            while queue and queue[-1][0] < dp[i]:
                queue.pop()
            queue.append((dp[i], i))

        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.constrainedSubsetSum([10, 2, -10, 5, 20], 2))
    print(solution.constrainedSubsetSum([-1, -2, -3], 1))
    print(solution.constrainedSubsetSum([10, -2, -10, -5, 20], 2))
