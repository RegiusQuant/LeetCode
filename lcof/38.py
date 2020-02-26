# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 上午10:07
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 38.py
# @Desc    : 说明

from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s:
            return []
        if len(s) == 1:
            return [s]
        s = ''.join(sorted(s))
        return self.helper(s)

    def helper(self, s: str):
        if len(s) == 1:
            return s
        result = []
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue
            temp = self.helper(s[:i] + s[i + 1:])
            for t in temp:
                result.append(s[i] + t)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.permutation('aabcc'))
