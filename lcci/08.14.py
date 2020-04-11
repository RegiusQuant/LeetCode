# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 上午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.14.py
# @Desc    : 说明

from functools import lru_cache


class Solution:
    def __init__(self):
        self.ops = {
            '&': {
                True: [(True, True)],
                False: [(True, False), (False, False), (False, True)],
            },
            '|': {
                True: [(True, False), (True, True), (False, True)],
                False: [(False, False)]
            },
            '^': {
                True: [(True, False), (False, True)],
                False: [(True, True), (False, False)],
            }
        }

    def countEval(self, s: str, result: int) -> int:
        return self.helper(s, result)

    @lru_cache(maxsize=None)
    def helper(self, expression, result):
        if len(expression) == 1:
            return int(bool(int(expression)) == result)

        total = 0
        for i in range(len(expression)):
            if expression[i] in self.ops:
                for l, r in self.ops[expression[i]][result]:
                    total += self.helper(expression[:i], l) * self.helper(expression[i + 1:], r)
        return total


if __name__ == '__main__':
    solution = Solution()
    print(solution.countEval('1^0|0|1', 0))
    print(solution.countEval("0&0&0&1^1|0", 1))