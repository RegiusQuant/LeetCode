# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 上午10:00
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 1111.py
# @Desc    : 说明

from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result, depth = [], 0
        for x in seq:
            if x == '(':
                depth += 1
                result.append(depth % 2)
            else:
                result.append(depth % 2)
                depth -= 1
        return result
