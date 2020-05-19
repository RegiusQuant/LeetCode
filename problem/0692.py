# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 下午12:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0692.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        temp = list(Counter(words).items())
        temp.sort(key=lambda x: (-x[1], x[0]))
        return [x[0] for x in temp][:k]


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    print(solution.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
