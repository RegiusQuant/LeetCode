# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 下午2:08
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        for i in range(1, len(s)):
            result = max(s[:i].count('0') + s[i:].count('1'), result)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxScore('011101'))
    print(solution.maxScore('00111'))
    print(solution.maxScore('1111'))
    print(solution.maxScore('00'))
