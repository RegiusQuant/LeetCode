# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 上午10:15
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0139.py
# @Desc    : 说明

from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        @lru_cache(None)
        def check(s):
            if not s:
                return True

            for i in range(len(s)):
                if s[:i + 1] in wordDict and check(s[i + 1:]):
                    return True
            return False

        return check(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))
    print(solution.canFinish(2, [[1, 0], [0, 1]]))
