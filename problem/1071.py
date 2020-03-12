# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 上午10:30
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1071.py
# @Desc    : 说明

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for i in range(min(len1, len2), 0, -1):
            if len1 % i != 0 or len2 % i != 0:
                continue
            if str1[:i] != str2[:i]:
                continue
            if str1[:i] * (len1 // i) == str1 and str2[:i] * (len2 // i) == str2:
                return str1[:i]
        return ""


if __name__ == '__main__':
    solution = Solution()
    print(solution.gcdOfStrings('ABCABC', 'ABC'))
    print(solution.gcdOfStrings('ABABAB', 'AB'))
    print(solution.gcdOfStrings('LEET', 'CODE'))
