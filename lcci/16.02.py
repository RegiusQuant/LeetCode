# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 下午1:25
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.02.py
# @Desc    : 说明

from typing import List
from collections import Counter


class WordsFrequency:

    def __init__(self, book: List[str]):
        self.counter = Counter(book)

    def get(self, word: str) -> int:
        return self.counter[word]
