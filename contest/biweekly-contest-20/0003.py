# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 下午10:22
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 0003.py
# @Desc    : 说明

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        try:
            index = {w: s.index(w) for w in 'abc'}
            for i, w in enumerate(s):
                result += len(s) - max(index.values())
                index[w] = s.index(w, i + 1)
        except ValueError:
            return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfSubstrings('aaacb'))
    print(solution.numberOfSubstrings('abcabc'))
    print(solution.numberOfSubstrings('abc'))
