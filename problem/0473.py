# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 下午8:13
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0473.py
# @Desc    : 说明

from typing import List
from functools import lru_cache


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n, s = len(nums), sum(nums)
        e = s // 4
        if e * 4 != s:
            return False

        @lru_cache(None)
        def dfs(mask, done):
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += nums[i]

            if total > 0 and total % e == 0:
                done += 1
            if done == 3:
                return True

            result = False
            rem = e * (done + 1) - total
            for i in range(n):
                if (mask & (1 << i)) == 0 and nums[i] <= rem:
                    if dfs(mask | (1 << i), done):
                        result = True
                        break
            return result

        return dfs(0, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.makesquare([1, 1, 2, 2, 2]))
    print(solution.makesquare([3, 3, 3, 3, 4]))
    print(solution.makesquare([5, 5, 5, 5, 16, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4]))
