# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午2:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        x = min(C, G) - max(A, E)
        y = min(D, H) - max(B, F)
        total = (C - A) * (D - B) + (G - E) * (H - F)
        if x > 0 and y > 0:
            return total - x * y
        else:
            return total


if __name__ == '__main__':
    solution = Solution()
    print(solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))