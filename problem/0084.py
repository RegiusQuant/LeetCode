# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 下午8:04
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0084.py
# @Desc    : 说明

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        left, right = [0] * n, [0] * n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in reversed(range(n)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        return max((right[i] - left[i] - 1) * heights[i] for i in range(n))


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
