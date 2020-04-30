# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 上午10:37
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0125.py
# @Desc    : 说明

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join(x.lower() for x in s if x.isdigit() or x.isalpha())
        s = t
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(solution.isPalindrome("race a car"))
    print(solution.isPalindrome(""))
