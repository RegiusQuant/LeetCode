# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 上午11:13
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0939.py
# @Desc    : 说明


from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        s = set(map(tuple, points))
        result = float('inf')
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points[i + 1:]):
                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in s and (p2[0], p1[1]) in s:
                    result = min(result, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))
        return result if result < float('inf') else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]))
    print(solution.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]))
