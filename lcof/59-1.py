# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 上午10:01
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 59-1.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        queue = deque()
        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        result = [queue[0]]
        for i in range(k, len(nums)):
            if queue[0] == nums[i - k]:
                queue.popleft()
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            result.append(queue[0])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
