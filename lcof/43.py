# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 上午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 43.py
# @Desc    : 说明

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1

        s = str(n)
        highNum, otherNum, length = int(s[0]), int(s[1:]), len(s)

        if highNum == 1:
            firstCount = otherNum + 1
        else:
            firstCount = pow(10, length - 1)
        otherCount = highNum * (length - 1) * pow(10, length - 2)
        return firstCount + otherCount + self.countDigitOne(otherNum)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countDigitOne(12))
    print(solution.countDigitOne(100))
