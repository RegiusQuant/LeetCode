# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 下午5:06
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0069.py
# @Desc    : 说明

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, 2 ** 32
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
