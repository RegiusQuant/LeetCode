# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 下午1:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 58-1.py
# @Desc    : 说明

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.strip().split()))


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords('the sky is blue'))
