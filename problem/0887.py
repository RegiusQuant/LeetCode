# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 下午6:19
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0887.py
# @Desc    : 说明

from functools import lru_cache


class Solution:

    @lru_cache(None)
    def superEggDrop(self, K: int, N: int) -> int:
        if N == 0:
            return 0
        if K == 1:
            return N

        left, right = 1, N
        while left + 1 < right:
            x = (left + right) // 2
            t1 = self.superEggDrop(K - 1, x - 1)
            t2 = self.superEggDrop(K, N - x)

            if t1 < t2:
                left = x
            elif t1 > t2:
                right = x
            else:
                left = right = x
        return 1 + min(max(self.superEggDrop(K - 1, x - 1), self.superEggDrop(K, N - x)) for x in (left, right))


if __name__ == '__main__':
    solution = Solution()
    print(solution.superEggDrop(1, 2))
    print(solution.superEggDrop(2, 6))
    print(solution.superEggDrop(3, 14))
