# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 上午9:38
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0466.py
# @Desc    : 说明

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        c1, c2, idx = 0, 0, 0
        recall = dict()

        while True:
            c1 += 1
            for c in s1:
                if c == s2[idx]:
                    idx += 1
                    if idx == len(s2):
                        c2, idx = c2 + 1, 0

            if c1 == n1:
                return c2 // n2

            if idx in recall:
                p1, p2 = recall[idx]
                preLoop = (p1, p2)
                inLoop = (c1 - p1, c2 - p2)
                break
            else:
                recall[idx] = (c1, c2)

        result = preLoop[1] + (n1 - preLoop[0]) // inLoop[0] * inLoop[1]
        rest = (n1 - preLoop[0]) % inLoop[0]
        for i in range(rest):
            for c in s1:
                if c == s2[idx]:
                    idx += 1
                    if idx == len(s2):
                        result, idx = result + 1, 0
        return result // n2


if __name__ == '__main__':
    solution = Solution()
    print(solution.getMaxRepetitions('acb', 4, 'ab', 2))
