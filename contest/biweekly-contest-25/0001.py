# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 下午10:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
    print(solution.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
    print(solution.kidsWithCandies(candies=[12, 1, 12], extraCandies=10))
