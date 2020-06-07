# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 下午9:57
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        m = arr[(len(arr) - 1) // 2]
        arr = sorted(arr, key=lambda x: (abs(x - m), x), reverse=True)
        return arr[:k]


if __name__ == '__main__':
    solution = Solution()
    print(solution.getStrongest([1, 2, 3, 4, 5], 2))
    print(solution.getStrongest([1, 1, 3, 5, 5], 2))
    print(solution.getStrongest([6, 7, 11, 7, 6, 8], 5))
