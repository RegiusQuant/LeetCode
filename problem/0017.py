# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 上午9:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0017.py
# @Desc    : 说明


from typing import List


class Solution:
    def __init__(self):
        self.letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.result = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.dfs(digits, 0, '')
        return self.result

    def dfs(self, digits, index, curr_str):
        if index >= len(digits):
            self.result.append(curr_str)
            return

        for c in self.letters[digits[index]]:
            self.dfs(digits, index + 1, curr_str + c)
