# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 下午5:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0253.py
# @Desc    : 说明

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        meeting = []
        for s, e in intervals:
            meeting.append((s, 1))
            meeting.append((e, -1))
        meeting.sort()

        count, result = 0, 0
        for m in meeting:
            count += m[1]
            result = max(result, count)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print(solution.minMeetingRooms([[7, 10], [2, 4]]))
