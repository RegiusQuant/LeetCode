# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 下午1:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        temp = sorted(list(counter.values()))
        s = 0
        for i in range(len(temp)):
            s += temp[i]
            if s == k:
                return len(temp) - i - 1
            elif s > k:
                return len(temp) - i
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLeastNumOfUniqueInts([5, 5, 4], 1))
    print(solution.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))
