# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 下午9:51
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0096.py
# @Desc    : 说明

from functools import lru_cache


class Solution:

    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        result = 0
        for i in range(n):
            result += self.numTrees(i) * self.numTrees(n - i - 1)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees(3))
