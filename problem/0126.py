# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 下午9:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0126.py
# @Desc    : 说明

import string
from typing import List
from collections import deque, defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordList = set(wordList)
        cost = defaultdict(int)
        for w in wordList:
            cost[w] = len(wordList) + 1
        cost[beginWord] = 0

        queue = deque()
        queue.append([beginWord])
        result = []

        while queue:
            currWords = queue.popleft()
            if result and len(currWords) > len(result[0]):
                break

            if currWords[-1] == endWord:
                result.append(currWords)

            currWord = currWords[-1]
            for i in range(len(currWord)):
                for c in string.ascii_lowercase:
                    nextWord = currWord[:i] + c + currWord[i + 1:]
                    if nextWord != currWord and nextWord in wordList and cost[currWord] + 1 <= cost[nextWord]:
                        cost[nextWord] = cost[currWord] + 1
                        queue.append(currWords + [nextWord])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLadders('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution.findLadders('hot', 'dog', ["hot", "dog"]))
    print(solution.findLadders('a', 'c', ["a", "c"]))
