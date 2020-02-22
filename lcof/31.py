# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 上午11:04
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 31.py
# @Desc    : 说明

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, pos1, pos2 = [], 0, 0
        while pos1 < len(pushed) and pos2 < len(popped):
            while pos1 < len(pushed):
                stack.append(pushed[pos1])
                pos1 += 1
                if pushed[pos1 - 1] == popped[pos2]:
                    break
            while stack and pos2 < len(popped) and popped[pos2] == stack[-1]:
                stack.pop()
                pos2 += 1
        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(solution.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))