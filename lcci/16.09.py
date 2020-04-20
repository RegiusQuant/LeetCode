# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 上午10:57
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.09.py
# @Desc    : 说明

class Operations:

    def __init__(self):
        pass

    def calcSign(self, a, b):
        p = True
        if a < 0:
            p = not p
            a = self.minus(0, a)
        if b < 0:
            p = not p
            b = self.minus(0, b)
        return a, b, p

    def minus(self, a: int, b: int) -> int:
        if b < 0:
            b = int(str(b)[1:])
        else:
            b = int('-' + str(b))
        return a + b

    def multiply(self, a: int, b: int) -> int:
        a, b, p = self.calcSign(a, b)

        bits, result = 0, 0
        for c in reversed(str(b)):
            x, t = int(c), 0
            for i in range(x):
                t += a
            t = int(str(t) + '0' * bits)
            bits += 1
            result += t
        return result if p else self.minus(0, result)

    def divide(self, a: int, b: int) -> int:
        a, b, p = self.calcSign(a, b)
        result, curr = 0, 0
        for c in str(a):
            curr = self.multiply(10, curr) + int(c)
            count = 0
            while curr >= b:
                curr = self.minus(curr, b)
                count += 1
            result = self.multiply(10, result) + count
        return result if p else self.minus(0, result)


if __name__ == '__main__':
    oper = Operations()
    print(oper.minus(1, 2))
    print(oper.multiply(3, 4))
    print(oper.divide(5, -2))
