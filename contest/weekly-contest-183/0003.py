# -*- coding: utf-8 -*-
# @Time    : 2020/4/5 上午10:18
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counter = [a, b, c]
        result, prev = '', -1

        while True:
            curr, mx = -1, -1
            for i in [0, 1, 2]:
                if i == prev or counter[i] <= 0:
                    continue
                if counter[i] > mx:
                    mx = counter[i]
                    curr = i
            if curr == -1:
                break

            c = chr(ord('a') + curr)
            if mx >= 2 and mx == max(counter):
                result += c * 2
                counter[curr] -= 2
            else:
                result += c
                counter[curr] -= 1
            prev = curr
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestDiverseString(a=1, b=1, c=7))
    print(solution.longestDiverseString(a=2, b=2, c=1))
    print(solution.longestDiverseString(a=7, b=1, c=0))
    print(solution.longestDiverseString(a=1, b=2, c=1))
    print(solution.longestDiverseString(a=10, b=2, c=0))
