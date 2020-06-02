# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 上午10:09
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0204.py
# @Desc    : 说明

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        valid = [True] * n
        valid[0] = valid[1] = False
        for i in range(4, n, 2):
            valid[i] = False
        for i in range(3, n, 2):
            if not valid[i]:
                continue
            for j in range(3, n, 2):
                if i * j >= n:
                    break
                valid[i * j] = False
        return sum(valid)