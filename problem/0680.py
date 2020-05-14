# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 上午11:40
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0680.py
# @Desc    : 说明

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.check(s[left + 1: right + 1]) or self.check(s[left: right])
        return True

    def check(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.validPalindrome('aba'))
    print(solution.validPalindrome('abca'))
