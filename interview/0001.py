# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午1:35
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明


class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num //= x
        return num == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isUgly(6))
    print(solution.isUgly(8))
    print(solution.isUgly(14))
