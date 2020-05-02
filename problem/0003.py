# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 上午10:02
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        counter = Counter()
        left, right = 0, 0
        while right < len(s):
            counter[s[right]] += 1
            while counter[s[right]] == 2:
                counter[s[left]] -= 1
                left += 1
            right += 1
            result = max(result, right - left)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))
    print(solution.lengthOfLongestSubstring('bbbbb'))
    print(solution.lengthOfLongestSubstring('pwwkew'))
