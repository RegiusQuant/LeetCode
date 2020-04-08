# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 上午10:54
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.09.py
# @Desc    : 说明

from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.helper('', n, n)
        return self.result

    def helper(self, curr, left, right):
        if left == right == 0:
            self.result.append(curr)
            return

        if right > left:
            self.helper(curr + ')', left, right - 1)
        if left > 0:
            self.helper(curr + '(', left - 1, right)


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
