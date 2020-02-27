# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 下午4:05
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0022.py
# @Desc    : 说明

from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.dfs('', 0, 0, n)
        return self.result

    def dfs(self, s, leftCount, rightCount, n):
        if len(s) == 2 * n:
            self.result.append(s)
            return
        if leftCount < n:
            self.dfs(s + '(', leftCount + 1, rightCount, n)
        if leftCount > rightCount:
            self.dfs(s + ')', leftCount, rightCount + 1, n)


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))