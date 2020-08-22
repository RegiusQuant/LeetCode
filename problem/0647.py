# -*- coding: utf-8 -*-
# @Time       : 2020/08/19 23:11:58
# @Author     : RegiusQuant <315135833@qq.com>
# @Project    : LeetCode
# @File       : 0647.py
# @Description: 文件说明


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(2 * n - 1):
            left, right = i // 2, i // 2 + i % 2
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                result += 1
        return result
