# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 上午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0004.py
# @Desc    : 说明

from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        total = sum(digits)
        m1 = sorted([x for x in digits if x % 3 == 1])
        m2 = sorted([x for x in digits if x % 3 == 2])
        if total % 3 == 1:
            if len(m1) >= 1:
                digits.remove(m1[0])
            elif len(m2) >= 2:
                digits.remove(m2[0])
                digits.remove(m2[1])
            else:
                return ""
        elif total % 3 == 2:
            if len(m2) >= 1:
                digits.remove(m2[0])
            elif len(m1) >= 2:
                digits.remove(m1[0])
                digits.remove(m1[1])
            else:
                return ""
        if len(digits) == 0:
            return ""
        digits.sort(reverse=True)
        return str(int(''.join(map(str, digits))))


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestMultipleOfThree([8, 1, 9]))
    print(solution.largestMultipleOfThree([8, 6, 7, 1, 0]))
    print(solution.largestMultipleOfThree([1]))
    print(solution.largestMultipleOfThree([0, 0, 0, 0]))
