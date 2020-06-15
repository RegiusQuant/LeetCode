# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 下午1:38
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left, right, result = 0, max(bloomDay), max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            count, temp = 0, 0
            for x in bloomDay:
                if x <= mid:
                    count += 1
                    if count == k:
                        temp += 1
                        count = 0
                else:
                    count = 0
            if temp < m:
                left = mid + 1
            else:
                right = mid - 1
                result = min(result, mid)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDays([1, 10, 3, 10, 2], 3, 1))
    print(solution.minDays([1, 10, 3, 10, 2], 3, 2))
    print(solution.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))
    print(solution.minDays([1000000000, 1000000000], 1, 1))
