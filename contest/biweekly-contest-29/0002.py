# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 下午9:56
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        temp = []
        for i in range(1, n + 1):
            if n % i == 0:
                temp.append(i)
        if k > len(temp):
            return -1
        return temp[k - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.kthFactor(12, 3))
    print(solution.kthFactor(7, 2))
    print(solution.kthFactor(4, 4))
    print(solution.kthFactor(1, 1))
    print(solution.kthFactor(1000, 3))
