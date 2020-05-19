# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 下午12:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1249.py
# @Desc    : 说明

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        used = [True] * len(s)
        for i, c in enumerate(s):
            if c == ')':
                if not stack:
                    used[i] = False
                else:
                    stack.pop()
            elif c == '(':
                stack.append(i)
        for x in stack:
            used[x] = False
        result = [s[i] for i in range(len(s)) if used[i]]
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(solution.minRemoveToMakeValid("a)b(c)d"))
    print(solution.minRemoveToMakeValid("))(("))
    print(solution.minRemoveToMakeValid("(a(b(c)d)"))
