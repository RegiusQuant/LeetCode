# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 下午12:44
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0140.py
# @Desc    : 说明

from typing import List
from collections import deque


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        words = set(wordDict)

        dp = [False] * n
        for i in range(n):
            if s[:i + 1] in words:
                dp[i] = True
                continue
            for j in range(i):
                if dp[j] and s[j + 1: i + 1] in words:
                    dp[i] = True
                    break

        result = []
        if dp[-1]:
            queue = deque()
            self.helper(s, n - 1, words, result, queue, dp)
        return result

    def helper(self, s, p, words, result, path, dp):
        if s[:p + 1] in words:
            path.appendleft(s[:p + 1])
            result.append(' '.join(path))
            path.popleft()

        for i in range(p):
            if dp[i] and s[i + 1:p + 1] in words:
                path.appendleft(s[i + 1:p + 1])
                self.helper(s, i, words, result, path, dp)
                path.popleft()


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
