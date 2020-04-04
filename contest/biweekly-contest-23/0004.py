# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 下午10:21
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        result = 0
        for i in range(len(satisfaction)):
            temp = 0
            for j in range(i, len(satisfaction)):
                temp += satisfaction[j] * (j - i + 1)
            result = max(temp, result)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSatisfaction([-1, -8, 0, 5, -9]))
    print(solution.maxSatisfaction([4, 3, 2]))
    print(solution.maxSatisfaction([-1, -4, -5]))
    print(solution.maxSatisfaction([-2, 5, -1, 0, 3, -3]))
