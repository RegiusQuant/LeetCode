# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 上午10:06
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0008.py
# @Desc    : 说明

class Automaton:

    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.num = 0
        self.table = {
            'start': ['start', 'signed', 'number', 'end'],
            'signed': ['end', 'end', 'number', 'end'],
            'number': ['end', 'end', 'number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c: str):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c: str):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'number':
            self.num = self.num * 10 + int(c)
            self.num = min(self.num, 2 ** 31 - 1) if self.sign == 1 else min(self.num, 2 ** 31)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.num
