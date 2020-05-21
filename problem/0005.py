# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 上午9:55
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0005.py
# @Desc    : 说明

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left, right = self.helper(s, i, i)
            if right - left > end - start:
                start, end = left, right
            left, right = self.helper(s, i, i + 1)
            if right - left > end - start:
                start, end = left, right
        return s[start: end + 1]

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome('babad'))
    print(solution.longestPalindrome('cbbd'))
