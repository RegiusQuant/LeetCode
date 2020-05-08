# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 下午8:08
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0415.py
# @Desc    : 说明

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        result, carry = [], 0
        for i in range(max(len(num1), len(num2))):
            n1 = int(num1[i]) if i < len(num1) else 0
            n2 = int(num2[i]) if i < len(num2) else 0
            s = n1 + n2 + carry
            result.append(str(s % 10))
            carry = s // 10
        if carry:
            result.append(str(carry))
        return ''.join(reversed(result))


if __name__ == '__main__':
    solution = Solution()
    print(solution.addStrings('124', '256'))
