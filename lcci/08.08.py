# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 上午10:51
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 08.08.py
# @Desc    : 说明

from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.visit = set()

    def permutation(self, S: str) -> List[str]:
        self.helper('', S)
        return self.result

    def helper(self, curr, temp):
        if not temp:
            if curr not in self.visit:
                self.result.append(curr)
                self.visit.add(curr)
            return

        for i in range(len(temp)):
            self.helper(curr + temp[i], temp[:i] + temp[i + 1:])


if __name__ == '__main__':
    solution = Solution()
    print(solution.permutation('qqe'))