# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 下午10:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xc, yc = (x2 + x1) / 2, (y2 + y1) / 2
        vx, vy = abs(x_center - xc), abs(y_center - yc)
        hx, hy = (x2 - x1) / 2, (y2 - y1) / 2
        ux, uy = max(0., vx - hx), max(0., vy - hy)
        return ux * ux + uy * uy <= radius * radius


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkOverlap(
        radius=1, x_center=0, y_center=0, x1=1, y1=-1, x2=3, y2=1
    ))
    print(solution.checkOverlap(
        radius=1, x_center=0, y_center=0, x1=-1, y1=0, x2=0, y2=1
    ))
    print(solution.checkOverlap(
        radius=1, x_center=1, y_center=1, x1=-3, y1=-3, x2=3, y2=3
    ))
    print(solution.checkOverlap(
        radius=1, x_center=1, y_center=1, x1=1, y1=-3, x2=2, y2=-1
    ))
