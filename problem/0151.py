# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 上午10:14
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0151.py
# @Desc    : 说明

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed([w for w in s.split()]))


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))
    print(solution.reverseWords("  hello world!  "))
