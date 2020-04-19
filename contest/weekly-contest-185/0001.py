# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 下午1:04
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

class Solution:
    def reformat(self, s: str) -> str:
        a, b = [], []
        for c in s:
            if c.isdigit():
                a.append(c)
            else:
                b.append(c)

        if abs(len(a) - len(b)) > 1:
            return ''

        if len(a) < len(b):
            a, b = b, a
        result = ''
        for i in range(len(b)):
            result += a[i] + b[i]
        if len(a) > len(b):
            result += a[-1]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reformat("a0b1c2"))
    print(solution.reformat("leetcode"))
    print(solution.reformat("1229857369"))
    print(solution.reformat("covid2019"))
    print(solution.reformat("ab123"))
