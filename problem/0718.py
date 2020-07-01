# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 上午7:58
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0718.py
# @Desc    : 说明

from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def check(length):
            base, mod = 113, 10 ** 9 + 9

            ha = 0
            for i in range(length):
                ha = (ha * base + A[i]) % mod
            s, mult = {ha}, pow(base, length - 1, mod)
            for i in range(length, len(A)):
                ha = ((ha - A[i - length] * mult) * base + A[i]) % mod
                s.add(ha)

            hb = 0
            for i in range(length):
                hb = (hb * base + B[i]) % mod
            if hb in s:
                return True
            for i in range(length, len(B)):
                hb = ((hb - B[i - length] * mult) * base + B[i]) % mod
                if hb in s:
                    return True

            return False

        left, right, result = 0, min(len(A), len(B)), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left += 1
                result = mid
            else:
                right -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
