# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 下午7:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0] * 2 > target:
            return 0
        left, right, result = 0, len(nums) - 1, 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + self.powMod(2, right - left, (10 ** 9 + 7))) % (10 ** 9 + 7)
                left += 1
            else:
                right -= 1
        return result

    def powMod(self, a, x, m):
        if x == 0:
            return 1
        if x % 2 == 0:
            return self.powMod(a, x // 2, m) ** 2 % m
        else:
            return a * self.powMod(a, x - 1, m) % m


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSubseq([3, 5, 6, 7], 9))
    print(solution.numSubseq([3, 3, 6, 8], 10))
    print(solution.numSubseq([2, 3, 3, 4, 6, 7], 12))
    print(solution.numSubseq([5, 2, 4, 1, 7, 6, 8], 16))
