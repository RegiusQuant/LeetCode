# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 下午6:48
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 10.02.py
# @Desc    : 说明

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = defaultdict(list)
        for s in strs:
            strDict[tuple(sorted(s))].append(s)
        return list(strDict.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
