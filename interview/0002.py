# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 下午1:40
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        valid = [True] * n
        valid[0] = valid[1] = False
        for i in range(4, n, 2):
            valid[i] = False
        for i in range(3, n, 2):
            if not valid[i]:
                continue
            for j in range(3, n, 2):
                if i * j >= n:
                    break
                valid[i * j] = False
        return sum(valid)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(10))
    print(solution.countPrimes(499979))