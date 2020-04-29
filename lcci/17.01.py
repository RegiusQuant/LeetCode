# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 下午12:12
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 17.01.py
# @Desc    : 说明

class Solution:
    def add(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b != 0:
            c = a & b
            a ^= b
            b = (c << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)


if __name__ == '__main__':
    solution = Solution()
    print(solution.add(-1, 2))
