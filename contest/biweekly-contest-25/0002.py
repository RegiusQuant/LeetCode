# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 下午10:28
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0002.py
# @Desc    : 说明

class Solution:
    def maxDiff(self, num: int) -> int:
        minVal, maxVal = float('inf'), float('-inf')

        for i in range(10):
            for j in range(10):
                t = str(num)
                t = t.replace(str(i), str(j))
                t = int(t)
                if t != 0 and len(str(t)) == len(str(num)):
                    minVal = min(minVal, t)
                    maxVal = max(maxVal, t)
        return maxVal - minVal


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDiff(555))
    print(solution.maxDiff(9))
    print(solution.maxDiff(123456))
    print(solution.maxDiff(10000))
    print(solution.maxDiff(9288))
