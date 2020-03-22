# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 下午2:40
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

class Solution:
    def longestPrefix(self, s: str) -> str:
        n, m = len(s), int(1e9 + 7)
        h, t, p = [0] * (n + 1), [1] + [0] * n, 131
        for i in range(1, n + 1):
            h[i] = (h[i - 1] * p + (ord(s[i - 1]) - ord('a') + 1)) % m
            t[i] = (t[i - 1] * p) % m
        pos = 0
        for i in range(1, n):
            a = h[i]
            b = (h[-1] - h[-1 - i] * t[i] % m + m) % m
            if a == b:
                pos = i
        return s[:pos]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPrefix('ababab'))
