# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午1:35
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        result = 0
        for i in range(32, -1, -1):
            t1, t2 = m & (1 << i), n & (1 << i)
            if t1 == t2:
                if t1 and t2:
                    result += (1 << i)
            else:
                break
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.rangeBitwiseAnd(5, 7))
    print(solution.rangeBitwiseAnd(0, 1))
    print(solution.rangeBitwiseAnd(1, 3))
    print(solution.rangeBitwiseAnd(10, 11))
