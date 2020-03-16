# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 上午10:14
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 01.06.py
# @Desc    : 说明

class Solution:
    def compressString(self, S: str) -> str:
        result, count = '', 0
        for i, c in enumerate(S):
            if i == 0:
                result += c
                count = 1
            elif S[i] == S[i - 1]:
                count += 1
            else:
                result += str(count)
                result += c
                count = 1
        result += str(count)
        return result if len(result) < len(S) else S


if __name__ == '__main__':
    solution = Solution()
    print(solution.compressString('aabcccccaaa'))
    print(solution.compressString('abbccd'))