# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 下午8:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return 0

        result = 0
        for i in range(len(arr)):
            temp = arr[i]
            for j in range(i + 1, len(arr)):
                temp ^= arr[j]
                if temp == 0:
                    result += j - i
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countTriplets([2, 3, 1, 6, 7]))
    print(solution.countTriplets([1, 1, 1, 1, 1]))
