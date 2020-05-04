# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 上午10:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0045.py
# @Desc    : 说明

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        end, pos, result = 0, 0, 0
        for i in range(len(nums) - 1):
            pos = max(pos, i + nums[i])
            if i == end:
                end = pos
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.jump([2, 3, 1, 1, 4]))
