# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 上午10:53
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.13.py
# @Desc    : 说明

from typing import List


class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        if square1[0] > square2[0]:
            square1, square2 = square2, square1

        x1, y1, l1 = square1
        x2, y2, l2 = square2

        cx1, cy1 = x1 + l1 / 2, y1 + l1 / 2
        cx2, cy2 = x2 + l2 / 2, y2 + l2 / 2

        if cx1 == cx2:
            return [cx1, min(cy1 - l1 / 2, cy2 - l2 / 2), cx2, max(cy1 + l1 / 2, cy2 + l2 / 2)]
        elif cy1 == cy2:
            return [x1, cy1, max(x1 + l1, x2 + l2), cy2]
        else:
            k = (cy1 - cy2) / (cx1 - cx2)
            b = cy1 - k * cx1
            if abs(k) >= 1:
                ytop = max(cy1 + l1 / 2, cy2 + l2 / 2)
                ybot = min(cy1 - l1 / 2, cy2 - l2 / 2)
                xleft = (ybot - b) / k
                xright = (ytop - b) / k
                if xleft > xright:
                    xleft, xright = xright, xleft
                    ytop, ybot = ybot, ytop
                return [xleft, ybot, xright, ytop]
            else:
                xleft = x1
                xright = max(x1 + l1, x2 + l2)
                yright = k * xright + b
                yleft = k * xleft + b
                return [xleft, yleft, xright, yright]


if __name__ == '__main__':
    solution = Solution()
    print(solution.cutSquares([-1, -1, 2], [0, -1, 2]))