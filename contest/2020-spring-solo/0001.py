# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 下午3:00
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        result = 0
        for x in coins:
            result += (x + 1) // 2
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCount([4, 2, 1]))
    print(solution.minCount([2, 3, 10]))
