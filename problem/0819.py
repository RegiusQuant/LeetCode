# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 上午10:56
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0819.py
# @Desc    : 说明

import re
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counter = Counter()
        banned = set(banned)
        words = re.split("[!?',;. ]", paragraph)
        for word in words:
            word = word.lower()
            if word and word not in banned:
                counter[word] += 1
        return counter.most_common(1)[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))
