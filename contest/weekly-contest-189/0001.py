# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 下午12:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.busyStudent([1, 2, 3], [3, 2, 7], 4))
    print(solution.busyStudent([4], [4], 4))
    print(solution.busyStudent([4], [4], 5))
    print(solution.busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7))
    print(solution.busyStudent([9, 8, 7, 6, 5, 4, 3, 2, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10], 5))
