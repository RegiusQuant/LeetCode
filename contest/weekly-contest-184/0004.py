# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 下午4:58
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

class Solution:
    def numOfWays(self, n: int) -> int:
        if n == 1:
            return 12
        a = [6] + [0] * (n - 1)
        b = [6] + [0] * (n - 1)
        for i in range(1, n):
            a[i] = (a[i - 1] * 3 + b[i - 1] * 2) % int(1e9 + 7)
            b[i] = (a[i - 1] * 2 + b[i - 1] * 2) % int(1e9 + 7)
        return (a[-1] + b[-1]) % int(1e9 + 7)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numOfWays(2))
