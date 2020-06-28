# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 下午7:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = [x % k for x in arr]
        counter = Counter(arr)
        if counter[0] % 2 != 0:
            return False
        for i in range(1, k):
            if counter[i] != counter[k - i]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))
    print(solution.canArrange([1, 2, 3, 4, 5, 6], 7))
    print(solution.canArrange([1, 2, 3, 4, 5, 6], 10))
    print(solution.canArrange([-10, 10], 2))
    print(solution.canArrange([-1, 1, -2, 2, -3, 3, -4, 4], 3))
