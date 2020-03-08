# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

import string
from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        result, counter, asc = '', Counter(s), True
        while True:
            temp = ''
            charList = string.ascii_lowercase if asc else reversed(string.ascii_lowercase)
            for c in charList:
                if counter[c] > 0:
                    temp += c
                    counter[c] -= 1
            if not temp:
                break
            result += temp
            asc = not asc
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortString('aaaabbbbcccc'))
    print(solution.sortString('rat'))
    print(solution.sortString('leetcode'))
    print(solution.sortString('ggggggg'))
    print(solution.sortString('spo'))
