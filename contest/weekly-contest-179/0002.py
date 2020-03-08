# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 下午7:48
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        result, maxPos = 0, -1
        for i in range(len(light)):
            maxPos = max(maxPos, light[i])
            if i + 1 == maxPos:
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numTimesAllBlue([2, 1, 3, 5, 4]))
