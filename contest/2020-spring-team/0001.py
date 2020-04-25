# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 下午4:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        return len(Counter(scores))


if __name__ == '__main__':
    solution = Solution()
    print(solution.expectNumber([1, 2, 3]))
    print(solution.expectNumber([1, 1, 2]))
    print(solution.expectNumber([1, 1]))
