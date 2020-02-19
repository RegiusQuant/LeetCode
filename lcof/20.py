# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 下午2:14
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 20.py
# @Desc    : 说明

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip().lower()
        hasDot = hasExp = hasDigit = False
        for i, c in enumerate(s):
            if c in ['+', '-']:
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif c == '.':
                if hasDot or hasExp:
                    return False
                hasDot = True
            elif c == 'e':
                if hasExp or not hasDigit:
                    return False
                hasExp, hasDigit = True, False
            elif c.isdigit():
                hasDigit = True
            else:
                return False
        return hasDigit


if __name__ == '__main__':
    solution = Solution()
    print(solution.isNumber('+100'))
    print(solution.isNumber('5e2'))
    print(solution.isNumber('-123'))
    print(solution.isNumber('3.1416'))
    print(solution.isNumber('0123'))
    print(solution.isNumber('-1E-16'))
    print(solution.isNumber('12e'))
    print(solution.isNumber('1a3.14'))
    print(solution.isNumber('1.2.3'))
    print(solution.isNumber('+-5'))
    print(solution.isNumber('12e+5.4'))
