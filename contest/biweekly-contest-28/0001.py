# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 下午9:59
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices


if __name__ == '__main__':
    solution = Solution()
    print(solution.finalPrices([8, 4, 6, 2, 3]))
    print(solution.finalPrices([1, 2, 3, 4, 5]))
    print(solution.finalPrices([10, 1, 1, 6]))
