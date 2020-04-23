# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 上午10:13
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.15.py
# @Desc    : 说明

from typing import List
from collections import Counter


class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        result = [0, 0]
        a, b = Counter(solution), Counter(guess)
        for i in range(4):
            if solution[i] == guess[i]:
                result[0] += 1
                a[solution[i]] -= 1
                b[solution[i]] -= 1
        for c in 'RYGB':
            result[1] += min(a[c], b[c])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.masterMind('RGBY', 'GGRR'))
