# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 下午10:29
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0001.py
# @Desc    : 说明

class Solution:
    def maxPower(self, s: str) -> int:
        result = 0
        prev, temp = '\n', 1
        for c in s:
            if c == prev:
                temp += 1
            else:
                prev = c
                temp = 1
            result = max(result, temp)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPower('leetcode'))
    print(solution.maxPower('abbcccddddeeeeedcba'))
    print(solution.maxPower('triplepillooooow'))
    print(solution.maxPower('hooraaaaaaaaaaay'))
    print(solution.maxPower('tourist'))