# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 上午10:04
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 05.02.py
# @Desc    : 说明

class Solution:
    def printBin(self, num: float) -> str:
        result = '0.'
        for i in range(30):
            if num == 0:
                break
            num *= 2
            if num >= 1:
                result += '1'
                num -= 1
            else:
                result += '0'
        return result if num == 0 else 'ERROR'


if __name__ == '__main__':
    solution = Solution()
    print(solution.printBin(0.1))
