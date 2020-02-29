# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 上午11:00
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 48.py
# @Desc    : 说明

from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        counter, start, result = Counter(), 0, 0
        for i in range(len(s)):
            counter[s[i]] += 1
            while counter[s[i]] > 1:
                counter[s[start]] -= 1
                start += 1
            result = max(result, i - start + 1)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))
    print(solution.lengthOfLongestSubstring('bbbbb'))
    print(solution.lengthOfLongestSubstring('pwwkew'))
