# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 下午11:09
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0067.py
# @Desc    : 说明

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary('11', '1'))
