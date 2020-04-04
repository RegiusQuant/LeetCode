# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 下午10:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True

        counter = Counter(s)
        odd = 0
        for v in counter.values():
            if v % 2:
                odd += 1
        return odd <= k


if __name__ == '__main__':
    solution = Solution()
    print(solution.canConstruct('annabelle', 2))
    print(solution.canConstruct('leetcode', 3))
    print(solution.canConstruct('true', 4))
    print(solution.canConstruct('yzyzyzyzyzyzyzy', 2))
    print(solution.canConstruct('cr', 7))
    print(solution.canConstruct('messi', 3))