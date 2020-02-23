# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 下午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    print(solution.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
    print(solution.sortByBits([1000, 1000]))
    print(solution.sortByBits([2, 3, 5, 7, 11, 13, 17, 19]))
