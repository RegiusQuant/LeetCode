# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 上午10:45
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 44.py
# @Desc    : 说明

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n

        digitNum = 1
        while True:
            count = self.countLength(digitNum)
            if n < count:
                break
            n -= count
            digitNum += 1
        currNum = n // digitNum + pow(10, digitNum - 1)
        return int(str(currNum)[n % digitNum])

    def countLength(self, digitNum: int) -> int:
        if digitNum == 1:
            return 10
        return pow(10, digitNum - 1) * 9 * digitNum


if __name__ == '__main__':
    solution = Solution()
    print(solution.findNthDigit(3))
