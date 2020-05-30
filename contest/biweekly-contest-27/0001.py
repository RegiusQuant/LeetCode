# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 下午8:26
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


if __name__ == '__main__':
    solution = Solution()
    print(solution.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
    print(solution.canBeEqual([7], [7]))
    print(solution.canBeEqual([1, 12], [12, 1]))
    print(solution.canBeEqual([3, 7, 9], [3, 7, 11]))
    print(solution.canBeEqual([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]))
