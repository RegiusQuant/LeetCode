# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 下午1:31
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

from collections import Counter


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counter = Counter()
        result = 0
        for c in croakOfFrogs:
            if c == 'c':
                if counter['k'] > 0:
                    counter['k'] -= 1
                else:
                    result += 1
            elif c == 'r':
                counter['c'] -= 1
            elif c == 'o':
                counter['r'] -= 1
            elif c == 'a':
                counter['o'] -= 1
            elif c == 'k':
                counter['a'] -= 1
            counter[c] += 1

            if any(counter[x] < 0 for x in ['c', 'r', 'o', 'a', 'k']):
                break

        if any(counter[x] != 0 for x in ['c', 'r', 'o', 'a']):
            return -1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.minNumberOfFrogs('croakcroak'))
    print(solution.minNumberOfFrogs('crcoakroak'))
    print(solution.minNumberOfFrogs('croakcrook'))
    print(solution.minNumberOfFrogs('croakcroa'))