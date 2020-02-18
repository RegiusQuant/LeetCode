# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 上午9:24
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 17.py
# @Desc    : 说明

from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [x for x in range(1, 10 ** n)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.printNumbers(3))
