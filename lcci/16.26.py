# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 上午10:38
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.26.py
# @Desc    : 说明

import re


class Solution:
    def calculate(self, s: str) -> int:
        s = re.sub('([*+-/])', r' \1 ', s.replace(' ', '')).split()
        (first, *nums), operates = s[::2], s[1::2]
        queue, signs = [int(first)], []
        for opt, num in zip(operates, nums):
            if opt == '*':
                queue[-1] *= int(num)
            elif opt == '/':
                queue[-1] //= int(num)
            else:
                queue.append(int(num))
                signs.append(1 if opt == '+' else -1)
        return queue[0] + sum(i * j for i, j in zip(queue[1:], signs))


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate('3 + 2 * 2'))
