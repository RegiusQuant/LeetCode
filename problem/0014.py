# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 上午11:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0014.py
# @Desc    : 说明

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
