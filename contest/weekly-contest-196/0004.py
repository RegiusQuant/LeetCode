# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 下午2:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        if (len(num) * len(num) - 1) // 2 <= k:
            return ''.join(sorted(num))
        pos = num.index(min(num[:k + 1]))
        return num[pos] + self.minInteger(num[:pos] + num[pos + 1:], k - pos)
