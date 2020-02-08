# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 下午9:17
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0121.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        tmp, ret = prices[0], 0
        for p in prices:
            tmp = min(tmp, p)
            ret = max(ret, p - tmp)
        return ret


if __name__ == '__main__':
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))
    prices = [7, 6, 4, 3, 1]
    print(solution.maxProfit(prices))
