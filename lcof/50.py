# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 上午10:43
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 50.py
# @Desc    : 说明

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> str:
        counter = Counter(s)
        for x in s:
            if counter[x] == 1:
                return x
        return ' '


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstUniqChar('abaccdeff'))
    print(solution.firstUniqChar(''))
