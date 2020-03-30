# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 上午11:36
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n, result = len(rating), 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        result += 1
        return result
