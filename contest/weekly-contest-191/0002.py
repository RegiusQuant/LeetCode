# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 上午10:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0, h] + horizontalCuts
        verticalCuts = [0, w] + verticalCuts
        horizontalCuts.sort()
        verticalCuts.sort()

        hor, ver = [], []
        for i in range(1, len(horizontalCuts)):
            hor.append(horizontalCuts[i] - horizontalCuts[i - 1])
        for i in range(1, len(verticalCuts)):
            ver.append(verticalCuts[i] - verticalCuts[i - 1])
        return max(hor) * max(ver) % int(1e9 + 7)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea(5, 4, [1, 2, 4], [1, 3]))
    print(solution.maxArea(5, 4, [3, 1], [1]))
    print(solution.maxArea(5, 4, [3], [3]))
