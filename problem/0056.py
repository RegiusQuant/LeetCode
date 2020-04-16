# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 上午10:14
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0056.py
# @Desc    : 说明

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        result, temp = [], intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= temp[1]:
                temp[1] = max(temp[1], intervals[i][1])
            else:
                result.append(temp)
                temp = intervals[i]
        result.append(temp)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[15, 18], [1, 3], [2, 6], [8, 10]]))
    print(solution.merge([[1, 4], [4, 5]]))
