# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 下午8:27
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        c = set()
        for i in range(len(s) - k + 1):
            c.add(s[i:i + k])
        return len(c) == 2 ** k


if __name__ == '__main__':
    solution = Solution()
    print(solution.hasAllCodes('00110110', 2))
    print(solution.hasAllCodes('00110', 2))
    print(solution.hasAllCodes('0110', 1))
    print(solution.hasAllCodes('0110', 2))
    print(solution.hasAllCodes('0000000001011100', 4))
