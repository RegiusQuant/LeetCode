# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 下午10:20
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = defaultdict(list)
        for i in range(1, n + 1):
            count[self.countDigit(i)].append(i)

        maxGroup, result = 0, 0
        for k, v in count.items():
            if len(v) > maxGroup:
                maxGroup = len(v)
                result = 1
            elif len(v) == maxGroup:
                result += 1
        return result

    def countDigit(self, x: int) -> int:
        s, result = str(x), 0
        for c in s:
            result += int(c)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countLargestGroup(13))
    print(solution.countLargestGroup(2))
    print(solution.countLargestGroup(15))
    print(solution.countLargestGroup(24))
