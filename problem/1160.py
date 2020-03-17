# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 上午10:03
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1160.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        charCounter = Counter(chars)
        for w in words:
            wordCounter, flag = Counter(w), True
            for k, v in wordCounter.items():
                if v > charCounter[k]:
                    flag = False
                    break
            if flag:
                result += len(w)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countCharacters(["cat", "bt", "hat", "tree"], 'atach'))
