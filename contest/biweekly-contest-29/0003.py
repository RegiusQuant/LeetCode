# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 下午9:56
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        temp = []
        count, pos = 0, -1
        for i, x in enumerate(nums):
            if x == 1:
                count += 1
                if pos == -1:
                    pos = i
            else:
                if count != 0:
                    temp.append((pos, count))
                count, pos = 0, -1
        if count != 0:
            temp.append((pos, count))
        # print(temp)

        if len(temp) == 0:
            return 0
        if len(temp) == 1:
            if all(nums):
                return temp[0][1] - 1
            else:
                return temp[0][1]

        result = 0
        for i in range(len(temp)):
            result = max(result, temp[i][1])
            if i > 0 and temp[i - 1][0] + temp[i - 1][1] + 1 == temp[i][0]:
                result = max(result, temp[i - 1][1] + temp[i][1])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestSubarray([1, 1, 0, 1]))
    print(solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
    print(solution.longestSubarray([1, 1, 1]))
    print(solution.longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1]))
    print(solution.longestSubarray([0, 0, 0]))
    print(solution.longestSubarray([1, 0, 0, 0, 0]))