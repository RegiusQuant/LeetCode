# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 上午8:32
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0301.py
# @Desc    : 说明

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        currLevel = {s}
        while True:
            temp = list(filter(check, currLevel))
            if temp:
                return temp

            nextLevel = set()
            for s in currLevel:
                for i, c in enumerate(s):
                    if s[i] in '()':
                        nextLevel.add(s[:i] + s[i + 1:])
            currLevel = nextLevel


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeInvalidParentheses("()())()"))
    print(solution.removeInvalidParentheses("(a)())()"))
    print(solution.removeInvalidParentheses(")("))
