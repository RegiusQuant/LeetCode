# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 上午12:01
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0093.py
# @Desc    : 说明

from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.dfs(s, 0, [])
        return ['.'.join(s) for s in self.result]

    def dfs(self, s, n, rec):
        if n == 4:
            if s == "":
                self.result.append(rec)
            return

        if len(s) >= 1:
            self.dfs(s[1:], n + 1, rec + [s[0]])
        if len(s) >= 2 and 10 <= int(s[:2]):
            self.dfs(s[2:], n + 1, rec + [s[:2]])
        if len(s) >= 3 and 100 <= int(s[:3]) <= 255:
            self.dfs(s[3:], n + 1, rec + [s[:3]])


if __name__ == '__main__':
    solution = Solution()
    print(solution.restoreIpAddresses('25525511135'))
