# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 上午10:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0042.py
# @Desc    : 说明

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result, stack = 0, []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                curr, prev = i, stack[-1]
                stack.pop()
                if not stack:
                    break
                dist = curr - stack[-1] - 1
                h = min(height[curr], height[stack[-1]]) - height[prev]
                result += dist * h
            stack.append(i)
        return result
