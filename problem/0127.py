# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 上午11:35
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0127.py
# @Desc    : 说明

import string
from typing import List
from collections import deque


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList = set(wordList)
        queue = deque([(beginWord, 1)])

        while queue:
            currWord, length = queue.popleft()
            if currWord == endWord:
                return length

            for i in range(len(currWord)):
                for c in string.ascii_lowercase:
                    nextWord = currWord[:i] + c + currWord[i + 1:]
                    if nextWord in wordList:
                        queue.append((nextWord, length + 1))
                        wordList.remove(nextWord)
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution.ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
