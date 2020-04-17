# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 上午10:44
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0055.py
# @Desc    : 说明

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        pos = 0
        for i in range(n):
            if i > pos:
                break
            pos = max(pos, i + nums[i])
            if pos >= n - 1:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump([2, 3, 1, 1, 4]))
    print(solution.canJump([3, 2, 1, 0, 4]))
