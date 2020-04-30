# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 上午10:23
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0202.py
# @Desc    : 说明

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set([n])
        while n != 1:
            c = 0
            while n != 0:
                c += (n % 10) ** 2
                n //= 10
            if c in s:
                return False
            s.add(c)
            n = c
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(19))
