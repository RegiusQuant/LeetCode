# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 上午10:18
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

class Solution:
    def numSteps(self, s: str) -> int:
        x = int(s, 2)
        result = 0
        while x != 1:
            if x % 2:
                x += 1
            else:
                x //= 2
            result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSteps('1'))
