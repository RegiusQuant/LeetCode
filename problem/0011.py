# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 下午12:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0011.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, result = 0, len(height) - 1, 0
        while left < right:
            result = max(result, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
