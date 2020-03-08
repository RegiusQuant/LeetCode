# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from collections import defaultdict


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        stateDict = defaultdict(int)
        stateDict[0] = -1
        currState, result = 0, 0
        for i, c in enumerate(s):
            if c in ['a', 'e', 'i', 'o', 'u']:
                currState ^= (1 << (ord(c) - ord('a')))
            if currState in stateDict:
                result = max(result, i - stateDict[currState])
            else:
                stateDict[currState] = i
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findTheLongestSubstring('eleetminicoworoep'))
    print(solution.findTheLongestSubstring('leetcodeisgreat'))
    print(solution.findTheLongestSubstring('bcbcbc'))
    print(solution.findTheLongestSubstring('aeiouaeiou'))
    print(solution.findTheLongestSubstring('aei'))
