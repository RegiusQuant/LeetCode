# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 下午1:57
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.10.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        counter = Counter()
        for i in range(len(birth)):
            for j in range(birth[i], death[i] + 1):
                counter[j] += 1
        items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        return items[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxAliveYear([1900, 1901, 1950], [1948, 1951, 2000]))
